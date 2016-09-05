import functools
import collections
from pyjs import JSObject


class memorize(object):
    '''
    Source:https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
    Decorator. Caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''

    def __init__(self,cache=None):
        if not isinstance(cache, dict):
            self._cache = dict()
        else:
            self._cache = cache

    @property
    def cache(self):
        return self._cache

    @property
    def used_cashe(self):
        return self._used_cashe

    def __call__(self, func):

        self._func = func

        @functools.wraps(func)
        def wrapper(*args,**kwargs):

            use_func_cashe = kwargs["use_func_cashe"] if "use_func_cashe" in kwargs else True

            key = ( tuple(args), frozenset(kwargs.items()) )

            self._used_cashe = False

            if not isinstance(key, collections.Hashable):
                # uncacheable. a list, for instance.
                # better to not cache than blow up.
                return func(*args,**kwargs)

            if use_func_cashe and key in self._cache:
                self._used_cashe = True
                return self._cache[key]

            else:
                value = func(*args,**kwargs)
                self._cache[key] = value
                return value

        return wrapper

    def __repr__(self):
       '''Return the function's docstring.'''
       return self.func.__doc__
    def __get__(self, obj, objtype):
       '''Support instance methods.'''
       return functools.partial(self.__call__, obj)

    def __contains__(self,item):
        return self._cache.__contains__(item)

    def update(self,new_cache):
        self._cache.update(new_cache)

    def clear(self):
        self._cache = dict()
