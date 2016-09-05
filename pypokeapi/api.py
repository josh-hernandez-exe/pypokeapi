#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" pypokeapi.api

User interaction with this package is done through this file.
"""

from pypokeapi.request import make_request
from pypokeapi.exceptions import ResourceNotFoundError

if __debug__:
    import pdb

VALID_VERSIONS=frozenset(["v1","v2"])

_API_INSTANCES = dict()

class PokeApi(object):

    def __init__(self,version):

        version = validate_version(version)

        self._version = version
        self._endpoints = None

    @property
    def version(self):
        return self._version

    @property
    def endpoints(self):
        return self._endpoints

    def _initialize_endpoints(self):
        data = make_request(version=self.version,json_output=True)
        self._endpoints = frozenset(data.keys())

    def get(self,endpoint="",param=""):
        """
        Make a request to the PokeAPI server and return the requested resource
        """

        if self.endpoints is None:
            self._initialize_endpoints()

        if self.version == "v2":
            endpoint = endpoint.replace("_","-")

        if endpoint in self.endpoints:

            data = make_request(
                version=self.version,
                endpoint=endpoint,
                param=param,
            )
            return data

        else:
            raise ResourceNotFoundError("An invalid argument was passed")


def validate_version(version):
    if isinstance(version,int):
        version = "v{number:d}".format(number=version)

    elif not isinstance(version, str):
        raise Exception("Not a valid version")

    if version not in VALID_VERSIONS:
        raise Exception("Not a valid version")

    return version


def get(endpoint="",param="",version=""):
    
    version = validate_version(version)

    if version not in _API_INSTANCES and version in VALID_VERSIONS:
        api_instance = PokeApi(version)
        _API_INSTANCES[version] = api_instance
    else:
        api_instance = _API_INSTANCES[version]

    return api_instance.get(
        endpoint=endpoint,
        param=param,
    )
