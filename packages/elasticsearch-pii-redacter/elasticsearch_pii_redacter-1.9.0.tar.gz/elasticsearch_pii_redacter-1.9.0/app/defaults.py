"""App Defaults"""
from six import string_types
from voluptuous import All, Any, Boolean, Coerce, Optional, Range, Required, Schema

TRACKING_INDEX = 'redactions-tracker'

# pylint: disable=E1120

# Configuration file: logging
def config_logging():
    """
    Logging schema with defaults:

    .. code-block:: yaml

        logging:
          loglevel: INFO
          logfile: None
          logformat: default
          blacklist: ['elastic_transport', 'urllib3']

    :returns: A valid :py:class:`~.voluptuous.schema_builder.Schema` of all acceptable values with
        the default values set.
    :rtype: :py:class:`~.voluptuous.schema_builder.Schema`
    """
    return Schema(
        {
            Optional('loglevel', default='INFO'):
                Any(None, 'NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL',
                    All(Coerce(int), Any(0, 10, 20, 30, 40, 50))
                    ),
            Optional('logfile', default=None): Any(None, *string_types),
            Optional('logformat', default='default'):
                Any(None, All(Any(*string_types), Any('default', 'ecs'))),
            Optional('blacklist', default=['elastic_transport', 'urllib3']): Any(None, list),
        }
    )

def index_pattern():
    """An index pattern to search and redact data from
    """
    return {
        Optional(Any(*string_types)): {
            Required('pattern'): Any(*string_types),
            Required('query'): dict,
            Required('fields'): [Any(*string_types)],
            Required('message', default='REDACTED'): Any(*string_types),
            Optional('delete', default=True): Any(bool, All(Any(*string_types), Boolean())),
            Required('expected_docs'): All(Coerce(int), Range(min=1, max=32768)),
            Optional('restore_settings', default=None): Any(dict, None)
        }
    }

def index_settings():
    """The Elasticsearch index settings for the progress/status tracking index"""
    return {'index': {'number_of_shards': '1'}}

def status_mappings():
    """The Elasticsearch index mappings for the progress/status tracking index"""
    return {
        "properties": {
            "job": {"type": "keyword"},
            "task": {"type": "keyword"},
            "join_field": { 
                "type": "join",
                "relations": {
                    "job": "task" 
                }
            },
            "cleanup": {"type": "keyword"},
            "completed": {"type": "boolean"},
            "end_time": {"type": "date"},
            "errors": {"type": "boolean"},
            "dry_run": {"type": "boolean"},
            "index": {"type": "keyword"},
            "logs": {"type": "text"},
            "start_time": {"type": "date"}
        },
        "dynamic_templates": [
            {
                "configuration": {
                    "path_match":   "config.*",
                    "mapping": {
                        "type": "keyword",
                        "index": False
                    }
                }
            }
        ]
    }

def redaction_schema():
    """The full voluptuous Schema for a redaction file
    """
    return Schema(
        {
            Required('redactions'): [index_pattern()]
        }
    )

def progress_filename():
    """The name of the file tracking progress
    """
    return 'script_progress'

def snapshot_filename():
    """The name of the file tracking which snapshots should be deleted
    """
    return 'snapshotstodelete'
