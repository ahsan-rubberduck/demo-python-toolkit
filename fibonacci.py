"""Fibonacci sequence generators."""


def fib_iterative(n):
    """Return the first ``n`` Fibonacci numbers as a list."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def fib_nth(n):
    """Return the ``n``-th Fibonacci number (0-indexed)."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_generator():
    """Yield Fibonacci numbers indefinitely."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
