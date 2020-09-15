from __future__ import absolute_import
from __future__ import unicode_literals

from pylint import checkers
from pylint import interfaces

PREFERRED_REQUEST_METHODS = {
    'requests.delete': 'utils.delete_request',
    'requests.get': 'utils.get_request',
    'requests.head': 'utils.head_request',
    'requests.post': 'utils.post_request',
    'requests.put': 'utils.put_request'
}


class LoggerUsageChecker(checkers.BaseChecker):
    """Custom pylint checker which checks for the usage of logger function
    and warns devlopers not to log critical info on server.
    """

    __implements__ = interfaces.IAstroidChecker

    name = 'logging-info-on-server'
    priority = -1
    msgs = {
        'W0001': (
            'Logging data on server can lead to data breach.',
            'logging-info-on-server',
            'Logging data on server can lead to data breach from the '
            'network. Make sure that you are not logging critical informations.'
        )
    }

    def visit_call(self, node):
        """Visits each function call in a lint check.

        Args:
            node: Call. The current function call node.
        """
        node_string = node.as_string()
        if 'logging.' in node_string:
            self.add_message('logging-info-on-server', node=node)


class HttpRequestChecker(checkers.BaseChecker):
    """Custom pylint checker to promote using wrapper functions
    for HTTP requests.
    """

    __implements__ = interfaces.IAstroidChecker

    name = 'consider-using-request-wrapper'  # pylint: disable=trailing-whitespace
    priority = -1
    msgs = {
        'W0002': (
            'Use %s method instead of %s.',
            'consider-using-request-wrapper',
            'All HTTP request should be called through the wrapper '
            'functions in utils module.'
        )
    }

    def visit_call(self, node):
        """Visits each function call in a lint check.

        Args:
            node: Call. The current function call node.
        """
        for function_name in PREFERRED_REQUEST_METHODS:
            if function_name in node.as_string():
                self.add_message(
                    'consider-using-request-wrapper', node=node, args=(
                        PREFERRED_REQUEST_METHODS[function_name],
                        function_name))
                return



def register(linter):
    """Registers the checker with pylint.

    Args:
        linter: Pylinter. The Pylinter object.
    """
    linter.register_checker(LoggerUsageChecker(linter))
    linter.register_checker(HttpRequestChecker(linter))
