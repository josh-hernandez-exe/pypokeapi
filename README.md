## pypokeapi
A python wrapper for the api provided by pokeapi.co. Caching of requests is built in. Much of the code was inspired by https://github.com/PokeAPI/pykemon. Models were removed in favor of supporting both v1 and v2.

## Installation

First you are going to need a library I wrote. Clone the project using your prefered method

```bash
# using https
git clone https://github.com/josh-hernandez-exe/pyjs.git
# using ssh
git clone git@github.com:josh-hernandez-exe/pyjs.git
cd pyjs
python setup.py install
```

Then do the same with the pypokeapi project.

```bash
# using https
git clone https://github.com/josh-hernandez-exe/pypokeapi.git
# using ssh
git clone git@github.com:josh-hernandez-exe/pypokeapi.git
cd pypokeapi
python setup.py install
```

## Examples

```python
>>> import pypokeapi
>>> result = pypokeapi.get(pokemon='bulbasaur')
>>> print(list(result.keys_()))
[u'abilities', u'weight', u'location_area_encounters', u'height', u'is_default', u'moves', u'base_experience', u'types', u'name', u'game_indices', u'stats', u'held_items', u'id', u'forms', u'species', u'order', u'sprites']
>>> print(result.moves[1].move.name)
u'swords-dance'
>>> print(result.moves[1].move.url)
u'https://pokeapi.co/api/v2/move/14/'
>>> move_result = pypokeapi.url_request(result.moves[1].move.url)
>>> print(list(move_result.keys_()))
[u'effect_changes', u'power', u'generation', u'stat_changes', u'past_values', u'meta', u'names', u'contest_combos', u'id', u'machines', u'name', u'pp', u'super_contest_effect', u'target', u'effect_entries', u'flavor_text_entries', u'effect_chance', u'contest_type', u'priority', u'damage_class', u'contest_effect', u'type', u'accuracy']
>>> print(move_result.flavor_text_entries[1].flavor_text)
A frenetic dance to uplift the fighting
spirit. This sharply raises the user’s
Attack stat.
```

You are able to save the cashe.

```python
pypokeapi.save_cache("/path/to/a/file.json")
```

You are also able to fill up the cashe from a previous session.

```python
pypokeapi.update_cache("/path/to/a/file.json")
```

You can set a default path for the cashe.

```python
pypokeapi.set_defualt_cashe_location("/path/to/default/file.json")
# The following functions can be passed nothing, and will use that file location.
pypokeapi.save_cache()
pypokeapi.update_cache()
```

The pypokeapi wrapper can wrtie to the default cashe location after a set interval of unique requests.

```python
pypokeapi.set_cache_write_frequency(10)
# So every 10 unique requests, a json file of cached data will be written to the defualt cashe location.
```

You can also clear the in memory cache.
```python
pypokeapi.clear_cache()
```

    clear_cache,
    save_cache,
    set_cache_write_frequency,
    set_defualt_cashe_location,
    set_protocol,
    update_cache,
    url_request,

## Notes

Caching is based of the uri's. For example a key in the cashe would be `api/v2/pokemon/1/`

For development, if you are running a local instance of PokeAPI, then you can modify the `_API_DOMAIN_` variable in `pypokeapi.request`.

```python
from pypokeapi import request
request._API_DOMAIN = "localhost" # Defualt set to "pokeapi.co"
```

By default, `https` is used for all requests. If you must use `http` then change the `_PROTOCOL` variable in `pypokeapi.request`.

```python
from pypokeapi import request
request._PROTOCOL = "http" # Defualt set to "https"
```