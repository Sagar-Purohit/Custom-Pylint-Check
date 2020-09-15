from __future__ import absolute_import
from __future__ import unicode_literals

import logging
import requests

import utils

CRITICAL_INFORMATION = "someImportantKey"

logging.info("Logging important key %s" % CRITICAL_INFORMATION)

requests.get("https://google.com")

utils.get_request("https://google.com")

X = 5

def FunctionName_():
    return requests.get("https://google.com")

class invalid_Class_Name():
    pass




