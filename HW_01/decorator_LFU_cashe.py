from collections import OrderedDict
import functools
import requests


def lfu_cache(max_limit: int):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = args[0]
            if cache_key in my_cache:
                # Update the call counter for the key
                key_to_freq[cache_key] += 1
                print(key_to_freq)
                # Move to the end of the list
                key_to_freq.move_to_end(cache_key, last=True)
                print(
                    f"------The data from cash: {my_cache[cache_key]} for url: {cache_key}"
                )
                return my_cache[cache_key]
            result = f(*args, **kwargs)
            # Remove if the limit is reached
            if len(my_cache) >= max_limit:
                # Determine the key with the least number of calls
                lfu_key = min(key_to_freq, key=key_to_freq.get)
                print(f"--------------Minimal key: {lfu_key}-------------")
                # Remove the item from the cache and the call counter
                my_cache.pop(lfu_key)
                key_to_freq.pop(lfu_key)
            # Add a new item to the cache and create a counter
            my_cache[cache_key] = result
            key_to_freq[cache_key] = 1
            print(f"My_cache : {my_cache}")
            print(f"Key_to_freq: {key_to_freq}")
            print(f" The data from url: {cache_key} and data: {result}")
            return result

        my_cache = OrderedDict()
        key_to_freq = OrderedDict()
        return deco

    return internal


@lfu_cache(max_limit=4)
def fetch_url(url: str, first_n: int = 100) -> bytes:
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


def main():
    list_url = [
        "https://www.ukr.net/",
        "https://lms.ithillel.ua/",
        "https://google.com/",
        "https://medium.com/",
        "https://dou.ua/",
    ]

    for _ in range(1):
        print(fetch_url(list_url[1]))
        print(fetch_url(list_url[0]))
    for _ in range(3):
        print(fetch_url(list_url[2]))
        print(fetch_url(list_url[3]))
    for _ in range(4):
        print(fetch_url(list_url[4]))
    for _ in range(1):
        print(fetch_url(list_url[0]))
        print(fetch_url(list_url[1]))

    """
    Minimal key must be: https://www.ukr.net/
    Key_to_freq must be: OrderedDict([('https://google.com/', 3), ('https://medium.com/', 3), 
    ('https://dou.ua/', 4), ('https://lms.ithillel.ua/', 1)]) 
    """
    help(fetch_url)


if __name__ == "__main__":
    main()
