"""
description: this module provides some tornado handlers.
"""

import inspect
import json
import os
import time
import decimal
import tornado.web

from pistar_echo_agent.utilities.constants.api_document import API_DOCUMENT_FIELD
from pistar_echo_agent.utilities.exceptions.webserver import ServerMissingDocumentFieldException, \
    ServerWrongArgumentValueException
from pistar_echo_agent.utilities.util.exception_util import trace_exception

from pistar_echo_agent.utilities.server.check_arguments import check_arguments
from pistar_echo_agent.utilities.server.get_arguments import get_arguments


def format_response(response):
    """
    description: this function is used to convert response to string.
    """
    if isinstance(response, (list, dict)):
        return json.dumps(response, indent=4, ensure_ascii=False)
    return str(response)


def create_request_handler(function, logger):
    """
    description: this function is used to create the request handler.
    """
    # load the document of the function.
    document = function.__document__

    # get the application name.
    application_name = '.'.join([function.__module__, function.__name__])

    # check document fields.
    required_fields = [
        API_DOCUMENT_FIELD.DESCRIPTION,
        API_DOCUMENT_FIELD.SUMMARY,
        API_DOCUMENT_FIELD.ARGUMENTS,
        API_DOCUMENT_FIELD.RESPONSE,
        API_DOCUMENT_FIELD.API_PATH,
        API_DOCUMENT_FIELD.METHODS,
        API_DOCUMENT_FIELD.STATUS
    ]
    for field_name in required_fields:
        if field_name not in document:
            raise ServerMissingDocumentFieldException(
                field_name=field_name,
                application_name=application_name
            )

    # initialize a request handler.
    key = '&'.join(document[API_DOCUMENT_FIELD.METHODS]) + \
          '@' + document[API_DOCUMENT_FIELD.API_PATH]

    class RequestHandler(tornado.web.RequestHandler):
        """
        description: this is the temporary dynamic class.
        """
        documents = {key: document}

        def write_error(self, status_code: int, **kwargs) -> None:
            if "reason" in kwargs:
                # in debug mode, try to send a traceback
                self.finish(
                    {"error_code": status_code, "error_msg": kwargs["reason"]}
                )
            else:
                self.finish(
                    {"error_code": status_code, "error_msg": self._reason}
                )

    # initialize methods.
    methods = document[API_DOCUMENT_FIELD.METHODS]

    # get api path.
    api_path = document[API_DOCUMENT_FIELD.API_PATH]

    # get arguments specification.
    specification = inspect.getfullargspec(function)

    # check arguments schema.
    check_arguments(
        document[API_DOCUMENT_FIELD.ARGUMENTS],
        specification,
        application_name
    )

    def wrapper(self, *args, **kwargs):
        try:
            arguments = get_arguments(
                self.request, specification, document, application_name
            )
        except BaseException as exception:
            trace_exception(exception=exception, logger=logger)
            self.send_error(status_code=400, reason=str(exception))
            return None

        start_time = time.time()
        try:
            response = function(**arguments)
        except ServerWrongArgumentValueException as exception:
            trace_exception(exception=exception, logger=logger)
            self.send_error(status_code=400, reason=str(exception))
            return None
        decimal.getcontext().rounding = decimal.ROUND_HALF_UP
        time_consuming = int(decimal.Decimal(str(time.time() - start_time)).quantize(decimal.Decimal("0.000")) * 1000)
        logger.info(f"The api \'{api_path}\' is called successfully in {time_consuming}ms.")
        status, response = response
        self.set_status(status)
        if API_DOCUMENT_FIELD.FILESERVER in document:
            self.set_header("Content-Type", "application/octet-stream")
            self.set_header("Content-Disposition", f"attachment:filename={os.path.basename(arguments.get('filename'))}")
        else:
            self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(format_response(response))
        self.finish()

    for method in methods:
        setattr(RequestHandler, method, wrapper)

    return api_path, RequestHandler
