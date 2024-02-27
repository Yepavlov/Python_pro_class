import functools
from collections import OrderedDict

import requests


class LFU:
    """
    LFU (Least Frequently Used) Cache Implementation:

    This LFU cache decorator is designed to provide a caching mechanism for function calls.
    The LFU caching strategy is based on the principle of evicting the least frequently used items
    from the cache when the cache reaches its maximum size. If there are more than two elements in the cache
    that have been used the same number of times, we delete an element using the LRU principle.
    """

    def __init__(self, max_size: int):
        """
        :param max_size: the maximal size of cache

        my_cache: the OrderedDict stores key-value pairs where the key is a URL,
        and the corresponding value is the response from our request function.

        key_to_freq: The OrderedDict stores key-value pairs, with the key being a URL and the corresponding value
        representing the frequency of times we invoke our function with that specific URL.
        """
        self.max_size = max_size
        self.my_cache = OrderedDict()
        self.key_to_freq = OrderedDict()

    def __call__(self, func):
        @functools.wraps(func)
        def deco(*args, **kwargs):
            cache_key = args[0]
            if cache_key in self.my_cache:
                self.key_to_freq[cache_key] += 1
                print(self.key_to_freq)
                self.key_to_freq.move_to_end(cache_key, last=True)
                print(
                    f"------The data from cash: {self.my_cache[cache_key]} for url: {cache_key}"
                )
                return self.my_cache[cache_key]
            result = func(*args, **kwargs)
            print(f" The data from url: {cache_key} and data: {result}")
            self.delete()
            self.update(cache_key, result)
            print(f"My_cache : {self.my_cache}")
            print(f"Key_to_freq: {self.key_to_freq}")
            return result

        return deco

    def delete(self):
        if len(self.my_cache) >= self.max_size:
            lfu_key = min(self.key_to_freq, key=self.key_to_freq.get)
            print(f"--------------Minimal key: {lfu_key}-------------")
            self.my_cache.pop(lfu_key)
            self.key_to_freq.pop(lfu_key)

    def update(self, key: str, value: str):
        self.my_cache[key] = value
        self.key_to_freq[key] = 1


@LFU(max_size=4)
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
