from django.core.cache import cache
from .cache_keys import *
from .cache_durations import *


def get_or_set_cache(queryset, serializer, cache_name: str, type_data: str, cache_duration: int):
    try:
        exist_cache = cache.get(cache_name)
        if exist_cache:
            return exist_cache
        else:
            data = queryset
            if type_data == 'list':
                new_cache = serializer(data, many=True).data
            elif type_data == 'detail':
                new_cache = serializer(data).data
            else:
                raise ValueError("invalid type of data, (ps. only list or detail)")

            cache.set(cache_name, new_cache, cache_duration)
            return new_cache

    except Exception as e:
        raise e


def clear_multiply_cache(name_cache_prefix):
    try:
        cache_keys = cache.keys(f"{name_cache_prefix}_*")
        for key in cache_keys:
            cache.delete(key)

    except Exception as e:
        raise e
