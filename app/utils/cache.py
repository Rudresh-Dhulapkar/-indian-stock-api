from cachetools import TTLCache

stock_cache = TTLCache(maxsize=100, ttl=60)

history_cache = TTLCache(maxsize=100, ttl=300)