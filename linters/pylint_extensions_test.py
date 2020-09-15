"""Unit tests for the pytlint_extensions module."""
from __future__ import absolute_import
from __future__ import unicode_literals

import unittest

import astroid
from pylint import testutils

import pylint_extensions


class LoggerUsageCheckerTests(unittest.TestCase):

    def setUp(self):
        super(LoggerUsageCheckerTests, self).setUp()
        self.checker_test_object = testutils.CheckerTestCase()
        self.checker_test_object.CHECKER_CLASS = (
            pylint_extensions.LoggerUsageChecker)
        self.checker_test_object.setup_method()

    def test_loggging_values_leads_to_pylint_warning(self):
        code = 'logging.info(\'Some ctritical data %s\' % CTRITICAL_INFO)'
        node_logging = astroid.extract_node(code)

        message = testutils.Message(
            msg_id='logging-info-on-server',
            node=node_logging)

        with self.checker_test_object.assertAddsMessages(message):
            self.checker_test_object.checker.visit_call(
                node_logging)


class HttpRequestCheckerTests(unittest.TestCase):

    def setUp(self):
        super(HttpRequestCheckerTests, self).setUp()
        self.checker_test_object = testutils.CheckerTestCase()
        self.checker_test_object.CHECKER_CLASS = (
            pylint_extensions.HttpRequestChecker)
        self.checker_test_object.setup_method()

    def test_check_throws_warning_for_not_using_wrapper_for_get_requests(self):
        code = """
            import requests

            url = 'https://someurl.com'
            requests.get(url) #@
        """
        node_get_request = astroid.extract_node(code)

        message_args = ('utils.get_request', 'requests.get')
        message = testutils.Message(
            msg_id='consider-using-request-wrapper',
            node=node_get_request,
            args=message_args)

        with self.checker_test_object.assertAddsMessages(message):
            self.checker_test_object.checker.visit_call(
                node_get_request)
    
    def test_check_throws_warning_for_not_using_wrapper_for_put_requests(self):
        code = """
            import requests

            url = 'https://someurl.com'
            requests.put(url) #@
        """
        node_put_request = astroid.extract_node(code)

        message_args = ('utils.put_request', 'requests.put')
        message = testutils.Message(
            msg_id='consider-using-request-wrapper',
            node=node_put_request,
            args=message_args)

        with self.checker_test_object.assertAddsMessages(message):
            self.checker_test_object.checker.visit_call(
                node_put_request)



if __name__ == '__main__':
    unittest.main()
