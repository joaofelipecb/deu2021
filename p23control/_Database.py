import p23control._Symbol

def get_by_id_with_cache(cache,symbol,id):
    if cache is not None:
        return cache
    resolved = p23control._Symbol.resolve(symbol)
    cache = resolved(1,1,1)
    return cache
