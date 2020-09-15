from __future__ import absolute_import
from __future__ import unicode_literals

import requests

# The whitelisted URLs to HTTPS requests.
WHITELISTED_URLS_PREFIX = [
    'https://github.com'
]

# The wait timeowut for the HTTPS requests.
MAX_WAIT_TIMEOUT = 5.0

def requests_wrapper(request):
    "A decorator to wrap the HTTP request methods."
    def validate_before_request(url, *args, **kwargs):
        url_is_valid = False
        for valid_url in WHITELISTED_URLS_PREFIX:
            if url.startswith(valid_url):
                url_is_valid = True
                break
        if not url_is_valid:
            raise Exception('URL is not whitelisted: %s' % url)
        if 'timeout' in kwargs.keys():
            if kwargs['kwargs'] > MAX_WAIT_TIMEOUT:
                raise Exception(
                    'The max wait timout is for request %s secs, '
                    'recieved %s' % MAX_WAIT_TIMEOUT)
        else:
            kwargs = dict(kwargs)
            kwargs.update({'timeout': MAX_WAIT_TIMEOUT})
        return request(url, *args, **kwargs)
    return validate_before_request


@requests_wrapper
def get_request(url, *args, timeout=MAX_WAIT_TIMEOUT, **kwargs):
    """A wrapper functionn for making GET request.

    Args:
        url: str. The URL to make GET request.

    Returns:
        requests.Response. The response of the GET request.
    """
    return requests.get(url, *args, timeout=timeout, **kwargs)  # pylint: disable=consider-using-request-wrapper


@requests_wrapper
def post_request(url, *args, timeout=MAX_WAIT_TIMEOUT, **kwargs):
    """A wrapper functionn for making POST request.

    Args:
        url: str. The URL to make POST request.

    Returns:
        requests.Response. The response of the POST request.
    """
    return requests.post(url, *args, timeout=timeout, **kwargs)  # pylint: disable=consider-using-request-wrapper


@requests_wrapper
def put_request(url, *args, timeout=MAX_WAIT_TIMEOUT, **kwargs):
    """A wrapper functionn for making PUT request.

    Args:
        url: str. The URL to make PUT request.

    Returns:
        requests.Response. The response of the PUT request.
    """
    return requests.put(url, *args, timeout=timeout, **kwargs)  # pylint: disable=consider-using-request-wrapper


@requests_wrapper
def head_request(url, *args, timeout=MAX_WAIT_TIMEOUT, **kwargs):
    """A wrapper functionn for making HEAD request.

    Args:
        url: str. The URL to make HEAD request.

    Returns:
        requests.Response. The response of the HEAD request.
    """
    return requests.head(url, *args, timeout=timeout, **kwargs)  # pylint: disable=consider-using-request-wrapper


@requests_wrapper
def delete_request(url, *args, timeout=MAX_WAIT_TIMEOUT, **kwargs):
    """A wrapper functionn for making DELETE request.

    Args:
        url: str. The URL to make DELETE request.

    Returns:
        requests.Response. The response of the DELETE request.
    """
    return requests.delete(url, *args, timeout=timeout, **kwargs)  # pylint: disable=consider-using-request-wrapper
