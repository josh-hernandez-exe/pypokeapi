#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" pypokeapi.request

This is the request factory for pypokeapi
All API calls made to the PokeAPI website go from here.
"""

import os
import requests

try:
    import simplejson as json
    from simplejson import JSONDecodeError
except ImportError:
    import json
    from json import JSONDecodeError

from pypokeapi.utils import memorize,JSObject


_API_DOMAIN = "pokeapi.co"
_URL_FORMAT = '{protocol}://{domain}/{endpoint}/'
_CASHE_FILE = os.path.join(
    os.path.expanduser("~"),
    "pypokeapi_cache.json"
)

_PROTOCOL="https"

# This value can be set to None, so that automatic caching isn't done.
_WRITE_FREQUENCY = None
_request_count = 0

request_cache = memorize()


@request_cache
def _request(uri):
    """
    Just a wrapper around the request.get() function
    """

    url = _URL_FORMAT.format(
        protocol=_PROTOCOL,
        domain=_API_DOMAIN
        endpoint=uri
    )

    r = requests.get(url)

    if r.status_code == 200:
        return _to_json(r.text)
    else:
        raise ResourceNotFoundError(
            "URL \'{url}\' responded with {status_code} error".format(
                url=url,
                status_code=str(r.status_code)
        ))

def _to_json(data):
    try:
        content = json.loads(data)
        return content
    except JSONDecodeError:
        raise JSONDecodeError('Error decoding data', data, 0)

def set_cache_write_frequency(frequency):
    global _WRITE_FREQUENCY
    if frequency is None or isinstance(frequency, int):
        _WRITE_FREQUENCY = frequency

def set_defualt_cashe_location(file_path):
    global _CASHE_FILE
    _CASHE_FILE = file_path

def save_cache(file_path=None):
    if file_path is None:
        file_path = _CASHE_FILE

    with open(file_path,"w") as stream:
        stream.write(json.dumps(request_cache.cache))

def update_cache(file_path=None):
    if file_path is None:
        file_path = _CASHE_FILE

    with open(file_path) as stream:
        request_cache = request_cache.update(json.loads(stream.read()))

def clear_cache():
    request_cache.clear()

def make_request(version="",endpoint="",param="",json_output=False):
    global _request_count

    if isinstance(param,(int,float)):
        param = str(param)    

    assert all(isinstance(item,str) for item in [version,endpoint,param])

    assert len(version)>0

    uri_list=["api",version.strip()]

    if endpoint:
        uri_list.append(endpoint.strip())
        if param:
            uri_list.append(param.strip())

    result =  _request("/".join(uri_list))

    _request_count += request_cache.used_cashe

    if not json_output:
        result = JSObject(result)

    if isinstance(_WRITE_FREQUENCY,int) and _request_count % _WRITE_FREQUENCY == 0:
        _request_count = 1
        save_cache()

    return result

def url_request(url,json_output=False):
    endpoint = ""
    param = ""

    try:
        temp = url.split("/api/")
        temp = temp[1].split("/")
        version = temp[0]
        if len(temp) > 1:
            endpoint = temp[1]

            if len(temp) > 2:
                param = temp[2]
    except:
        raise ResourceNotFoundError("Invalid url : \"{url}\"".format(url=url))

    return make_request(
        version=version,
        endpoint=endpoint,
        param=param,
        json_output=json_output,

    )
