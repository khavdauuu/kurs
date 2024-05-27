def cache_deco(func):
    memoized_results = {}
    def cached_func(*args, **kwargs):
        key = str((args, kwargs))
        if key not in memoized_results:
            memoized_results[key] = func(*args, **kwargs)
        return memoized_results[key]

    return cached_func

def solution(func_map, func_filter, data):
    filtered_data = (d for d in data if func_filter(d))
    mapped_data = (func_map(d) for d in filtered_data)
    return iter(mapped_data)
@cache_deco
def expensive_function(arg):
    return arg * arg

def is_even(number):
    return number % 2 == 0

def double(number):
 double(number):
    return number * 2

data = [1, 2, 3, 4, 5, 6]

for item in solution(double, is_even, data):
    print(item)