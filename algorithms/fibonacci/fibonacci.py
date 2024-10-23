"""..."""


def fibonacci_iterative(limit: int) -> int:
    prev = 0
    fib = 1

    for _ in range(limit):
        tmp = fib
        fib = fib + prev
        prev = tmp

    return fib


def fibonacci_recursive(limit: int, cnt: int = 0, fib: int = 1, prev: int = 0) -> int:
    if limit == cnt:
        return fib

    return fibonacci_recursive(limit, cnt + 1, fib + prev, fib)
