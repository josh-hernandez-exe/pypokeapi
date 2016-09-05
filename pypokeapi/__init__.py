#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Josh Hernandez'
__version__ = '0.1.0'
__license__ = 'GNU GENERAL PUBLIC LICENSE'

import six

from pypokeapi import api as _api
from pypokeapi.request import (
    clear_cache,
    save_cache,
    set_cache_write_frequency,
    set_defualt_cashe_location,
    update_cache,
    url_request,
)

_API_VERSION = "v2"

def get(endpoint="",param="",version="",**kwargs):
    version = version if version else _API_VERSION

    if endpoint:
        pass

    elif "endpoint" in kwargs:
        endpoint = kwargs["endpoint"]
        if "param" in kwargs:
            param = kwargs["param"]

    elif len(kwargs) == 1:
        endpoint,param = tuple(six.iteritems(kwargs))
    else:
        raise Exception("Too many key word arguments passed in.")


    return _api.get(
        endpoint=endpoint,
        param=param,
        version=version,
    )

def change_version(new_version):
    new_version = _api.validate_version(new_version)
    _API_VERSION = new_version

"""

========
pypokeapi
========

A Python wrapper for PokeAPI (http://pokeapi.co)

Usage:

>>> import pypokeapi
>>> pypokeapi.get(pokemon='bulbasaur')
<Pokemon - Bulbasaur>
>>> pypokeapi.get(pokemon_id=151)
<Pokemon - Mew>

"""
