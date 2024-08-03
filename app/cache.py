import redis

cache = redis.Redis(host='localhost', port=6379, db=0)

def get_cached_response(text, task):
    key = f"{task}:{text}"
    return cache.get(key)

def set_cached_response(text, task, response):
    key = f"{task}:{text}"
    cache.set(key, response)