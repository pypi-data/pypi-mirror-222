"""Helper Functions"""
import logging
import json
from inspect import stack
from datetime import datetime
import re
from shutil import get_terminal_size
import click
from es_client.defaults import VERSION_MAX, VERSION_MIN
from es_client.exceptions import ConfigurationError as esc_ConfigError
from es_client.builder import Builder
from es_client.helpers.schemacheck import SchemaCheck
from es_client.helpers.utils import ensure_list, get_yaml, prune_nones
from app.defaults import config_logging, redaction_schema
from app.exceptions import ClientException, ConfigurationException
from app.logtools import LogInfo, Blacklist

def build_script(message, fields):
    """Build a painless script for redacting fields by way of an update_by_query operation

    :param message: The text to put in place of whatever is in a field
    :param fields: The list of field names to act on

    :type message: str
    :type fields: list

    :rtype: dict
    :returns: A dictionary of ``{"source": (the assembled message), "lang": "painless"}``
    """
    msg = ""
    for field in fields:
        msg += f"ctx._source.{field} = '{message}'; "
    script = {"source": msg, "lang": "painless"}
    return script

def check_logging_config(config):
    """
    Ensure that the top-level key ``logging`` is in ``config`` before passing it to
    :py:class:`~.es_client.helpers.schemacheck.SchemaCheck` for value validation.

    :param config: Logging configuration data

    :type config: dict

    :returns: :py:class:`~.es_client.helpers.schemacheck.SchemaCheck` validated logging
        configuration.
    """

    if not isinstance(config, dict):
        click.echo(
            f'Must supply logging information as a dictionary. '
            f'You supplied: "{config}" which is "{type(config)}"'
            f'Using default logging values.'
        )
        log_settings = {}
    elif not 'logging' in config:
        click.echo('No "logging" setting in supplied configuration.  Using defaults.')
        log_settings = {}
    else:
        if config['logging']:
            log_settings = prune_nones(config['logging'])
        else:
            log_settings = {}
    return SchemaCheck(
        log_settings, config_logging(), 'Logging Configuration', 'logging').result()

def chunk_index_list(indices):
    """
    This utility chunks very large index lists into 3KB chunks.
    It measures the size as a csv string, then converts back into a list for the return value.

    :param indices: The list of indices

    :type indices: list

    :returns: A list of lists (each a piece of the original ``indices``)
    :rtype: list
    """
    chunks = []
    chunk = ""
    for index in indices:
        if len(chunk) < 3072:
            if not chunk:
                chunk = index
            else:
                chunk += "," + index
        else:
            chunks.append(chunk.split(','))
            chunk = index
    chunks.append(chunk.split(','))
    return chunks

def end_it(obj, success):
    """Close out the object here to avoid code repetition"""
    # Record task success or fail here for THIS task_id
    # Each index in per_index has its own status tracker
    if not success:
        err = True
        log = 'Check application logs for detailed report'
    else:
        err = False
        log = 'DONE'
    obj.end(success, errors=err, logmsg=log)

def get_client(
    configdict=None, configfile=None, autoconnect=False, version_min=VERSION_MIN,
    version_max=VERSION_MAX):
    """Get an Elasticsearch Client using :py:class:`es_client.Builder`

    Build a client out of settings from `configfile` or `configdict`
    If neither `configfile` nor `configdict` is provided, empty defaults will be used.
    If both are provided, `configdict` will be used, and `configfile` ignored.

    :param configdict: A configuration dictionary
    :param configfile: A configuration file
    :param autoconnect: Connect to client automatically
    :param verion_min: Minimum acceptable version of Elasticsearch (major, minor, patch)
    :param verion_max: Maximum acceptable version of Elasticsearch (major, minor, patch)

    :type configdict: dict
    :type configfile: str
    :type autoconnect: bool
    :type version_min: tuple
    :type version_max: tuple

    :returns: A client connection object
    :rtype: :py:class:`~.elasticsearch.Elasticsearch`
    """
    logger = logging.getLogger(__name__)
    logger.debug('Creating client object and testing connection')

    builder = Builder(
        configdict=configdict, configfile=configfile, autoconnect=autoconnect,
        version_min=version_min, version_max=version_max
    )

    try:
        builder.connect()
    except Exception as exc:
        logger.critical('Unable to establish client connection to Elasticsearch!')
        logger.critical('Exception encountered: %s', exc)
        raise ClientException from exc

    return builder.client

def get_field_matches(config, result):
    """Count docs which have the expected fields

    :param config: The config from the YAML file
    :param result: The query result dict

    :type config: dict
    :type result: dict

    :returns: The count of docs in ``result`` which have the identified fields
    :rtype: int
    """
    logger = logging.getLogger(__name__)
    logger.debug('Extracting doc hit count from result')
    doc_count = result['hits']['total']['value']
    for element in range(0, result['hits']['total']['value']):
        for field in config['fields']:
            if len(field.split('.')) > 1:
                logger.debug('Dotted field "%s" detected...', field)
                fielder = result['hits']['hits'][element]['_source']
                for key in field.split('.'):
                    # This should recursively look for each subkey
                    if key in fielder:
                        fielder = fielder[key]
                    else:
                        doc_count -= 1
                        break
            elif field not in list(result['hits']['hits'][element]['_source'].keys()):
                logger.debug('Fieldname "%s" NOT detected...', field)
                doc_count -= 1
            else:
                logger.debug('Root-level fieldname "%s" detected...', field)
    return doc_count

def get_fname():
    """Return the name of the calling function"""
    return stack()[1].function

def get_index_version(name):
    """Extract a redacted index's version name from the end of the index

    :param name: The index name

    :type name: str

    :returns: The integer value of the current index revision, or 0 if no version
    :rtype: int
    """
    # Anchor the end as 3 dashes, a v, and 3 digits, e.g. ---v001
    match = re.search(r'^.*---v(\d{3})$', name)
    if match:
        return int(match.group(1))
    return 0

def get_redactions(file):
    """Return valid dictionary of redactions from ``file`` after checking Schema

    :param file: YAML file with redactions to check

    :type file: str

    :rtype: dict

    :returns: Redactions configuration data
    """
    logger = logging.getLogger(__name__)
    logger.debug('Getting redactions YAML file')
    try:
        from_yaml = get_yaml(file)
    except esc_ConfigError as exc:
        msg = f'Unable to read and/or parse YAML REDACTIONS_FILE: {file} Exiting.'
        logger.critical(msg)
        raise ConfigurationException(msg) from exc
    return SchemaCheck(
        from_yaml, redaction_schema(), 'Redaction Configuration', 'redactions').result()

def get_width():
    """Determine terminal width"""
    # return dict(max_content_width=get_terminal_size()[0])
    return {"max_content_width": get_terminal_size()[0]}

def now_iso8601():
    """Get the current timestamp and return it in UTC ISO8601 time format with milliseconds"""
    iso8601 = datetime.utcnow().isoformat()
    return f'{iso8601[:-3]}Z'

def config_fieldmap(rw_val, key):
    """Return the function from this function/key map"""
    which = {
        'read': {
            'pattern': json.loads,
            'query': json.loads,
            'fields': json.loads,
            'message': str,
            'expected_docs': int,
            'restore_settings': json.loads,
            'delete': str
        },
        'write': {
            'pattern': json.dumps,
            'query': json.dumps,
            'fields': json.dumps,
            'message': str,
            'expected_docs': int,
            'restore_settings': json.dumps,
            'delete': str
        }
    }
    return which[rw_val][key]

def parse_job_config(config, behavior):
    """Parse raw config from the index. 
    
    Several fields are JSON escaped, so we need to fix it to put it in a dict.

    :param config: The raw config config
    :param behavior: ``read`` or ``write``

    :type config: dict
    :type behavior: str

    :rtype: dict

    :returns: JSON-(de)sanitized configuration dict
    """
    fields = [
        'pattern', 'query', 'fields', 'message', 'expected_docs', 'restore_settings', 'delete'
    ]
    doc = {}
    for field in fields:
        if field in config:
            func = config_fieldmap(behavior, field)
            doc[field] = func(config[field])
    return doc

def set_logging(log_opts):
    """Configure global logging options

    :param log_opts: Logging configuration data

    :type log_opts: dict

    :rtype: None
    """
    # Set up logging
    loginfo = LogInfo(log_opts)
    logging.root.addHandler(loginfo.handler)
    logging.root.setLevel(loginfo.numeric_log_level)
    _ = logging.getLogger('redacter.cli')
    # Set up NullHandler() to handle nested elasticsearch8.trace Logger
    # instance in elasticsearch python client
    logging.getLogger('elasticsearch8.trace').addHandler(logging.NullHandler())
    if log_opts['blacklist']:
        for bl_entry in ensure_list(log_opts['blacklist']):
            for handler in logging.root.handlers:
                handler.addFilter(Blacklist(bl_entry))

def strip_index_name(name):
    """Strip ``partial-``, ``restored-``, ``redacted-``, and trailing ``---v000`` from ``name``

    :param name: The index name

    :type name: str

    :returns: The "cleaned up" and stripped index name
    :rtype: str
    """
    retval = name.replace('partial-', '')
    retval = retval.replace('restored-', '')
    retval = retval.replace('redacted-', '')
    # Anchor the end as 3 dashes, a v, and 3 digits, e.g. ---v001
    match = re.search(r'^(.*)---v\d{3}$', retval)
    if match:
        retval = match.group(1)
    return retval
