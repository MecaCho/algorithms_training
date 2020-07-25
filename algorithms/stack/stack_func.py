import functools

@functools.lru_cache()
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)



if __name__ == '__main__':
    res = fib(1000)
    print(res)

