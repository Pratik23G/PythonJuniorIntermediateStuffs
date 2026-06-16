from functools import lru_cache, partial, reduce, wraps

@lru_cache(maxsize=128)
def slow_fast_square(n):
    print(f"We are computing the square {n}")
    return n * n


slow_fast_square(4)
print(slow_fast_square(4))

slow_fast_square(6)

#fibonacci example with lru_cache

@lru_cache
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print(fib(100))

print(fib(3))
