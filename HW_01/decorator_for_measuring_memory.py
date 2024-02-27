import functools
import tracemalloc
import requests


def used_memory_deco(func):
    """
    A decorator to measure the memory usage of a function using tracemalloc
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        # function call
        result = func(*args, **kwargs)
        # store displaying the memory
        memory_start, memory_end = tracemalloc.get_traced_memory()
        # count of memory used
        used_memory = (memory_end - memory_start) / 1000
        print(f"The function: {func.__name__} consumes {used_memory} Kb of memory")
        tracemalloc.stop()
        return result

    return wrapper


@used_memory_deco
def fetch_url(url, first_n=100):
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
    for url in list_url:
        fetch_url(url)
    help(fetch_url)


if __name__ == "__main__":
    main()
