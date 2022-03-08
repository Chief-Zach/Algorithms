def fib(n):
    n = n + 1
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a