from zq_config.backends import Backend
from importlib import import_module
from cachetools import cached, TTLCache
from threading import RLock

class NacosBackend(Backend):
    _client = None

    def __init__(self, **kwargs) -> None:
        self._client = import_module("nacos").NacosClient(**kwargs)

    @cached(cache=TTLCache(maxsize=4096, ttl=60), lock=RLock())
    def get(self, data_id, data_group="DEFAULT_GROUP"):
        return self._client.get_config(data_id, data_group)
