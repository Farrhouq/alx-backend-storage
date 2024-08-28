#!/usr/bin/env python3
"""This is the redis exercise file"""

import redis
import uuid
import typing
from functools import wraps


def count_calls(method: typing.Callable) -> typing.Callable:
    """This method counts number of methods
    called int the cache class"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: typing.Callable) -> typing.Callable:
    """Thisis the call history"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(f"{key}:inputs", str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(f"{key}:outputs", str(res))
        return res
    return wrapper


class Cache:
    """This is the redis class"""

    def __init__(self):
        """This is the constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """This is going to create a random key
        and save it and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: typing.Optional[typing.Callable] = None) -> typing.Union[
                    str, bytes, int, float]:
        """This is the get function to get a key"""
        val = self._redis.get(key)
        if fn is not None and val is not None:
            return fn(val)
        return val

    def get_str(self, key: str) -> str:
        """this function is used to get strings"""
        val = self.get(key, fn=lambda x: x.decode())
        return val

    def get_int(self, key: str) -> int:
        """This function is used to get integers"""
        val = self.get(key, fn=int)
        return val


def replay(method: typing.Callable) -> None:
    """This is used to view the history of the function"""
    key = method.__qualname__
    self = method.__self__
    inputs = self._redis.lrange(f"{key}:inputs", 0, -1)
    outputs = self._redis.lrange(f"{key}:outputs", 0, -1)

    print(f"{key} was called {len(inputs)} times:")
    for _in, _out in zip(inputs, outputs):
        print(f"{key}(*{_in.decode('utf-8')}) -> {_out.decode('utf-8')}")
