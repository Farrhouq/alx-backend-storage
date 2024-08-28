#!/usr/bin/env python3
"""This is the web redis"""

import requests
import redis
import typing
from functools import wraps


red = redis.Redis()


def cache_page(method: typing.Callable) -> typing.Callable:
    """Thisis used to cache th apge"""
    @wraps(method)
    def wrapper(*args, **kwargs):
        page = red.get(args[0])
        if page is not None:
            return page.decode('utf-8')
        else:
            page = method(*args)
            red.set(args[0], page, ex=10)
            return page
    return wrapper


@cache_page
def get_page(url: str) -> str:
    """Thisisi the function that gets the page"""
    res = requests.get(url).text
    red.incr(f'count:{url}')
    return res
