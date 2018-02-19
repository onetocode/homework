def fibonacci(n):
    a = 0
    b = 1
    while n:
        yield b
        a, b = b, a + b
        n -= 1