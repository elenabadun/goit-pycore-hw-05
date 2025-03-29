from functools import lru_cache


@lru_cache
def fibonacci(n):
    """
    The function calculates the corresponding Fibonacci numbers, 
    storing previous results in the cache using decoretor “lru_cache”
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print(fibonacci(15))
