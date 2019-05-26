# -*- coding: utf-8 -*-
# import json
from .exceptions.Exceptions import exception_coordinator
from .vars.Vars import AWS_REGION
from .start_run import start_run


config = {
    'function_name': 'start_run',
    'function_module': 'service',
    'function_handler': 'handler',
    'handler': 'service.handler',
    'region': AWS_REGION,
    'runtime': 'python3.6',
    'role': 'tibanna_lambda_init_role',
    'description': 'Tibanna pony update_ffmeta_awsem',
    'timeout': 300,
    'memory_size': 256
}


def metadata_only(event):
    # this relies on the fact that event contains and output key with output files
    assert event['metadata_only']
    assert event['output_files']
    return real_handler(event, None)


@exception_coordinator('start_run_awsem', metadata_only)
def handler(event, context):
    if event.get('push_error_to_end', True):
        event['push_error_to_end'] = True  # push error to end by default for pony
    return real_handler(event, context)


def real_handler(event, context):
    return start_run(event)