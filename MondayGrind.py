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


#Now we will use soome prefills - partial

def power(base, exp):
    return base ** exp

square = partial(power, exp = 2)
cube = partial(power, exp = 3)

print(square(4))
print(cube(2))


#simple analogy it makes brank spanking new function
#based off the mould of the original function

# 3 reduce - fold a sequence into a single value

finalOutcome = reduce(lambda acc, n: acc + n, [1,2,3,4,5], 0)
#we use reduce only when max, min, sum or math.prod don't cover most cases or no -built in can be used

print(finalOutcome)


#now warps - preserve the metadata when writing decorators

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@lru_cache(maxsize=32)
def fetch_url(url, retries, timeout):
    print(f"Printing out some content may tike some time")
    print(f"--- [Cache Miss] Actually running the heavy network code for {url} ---")
    return f"Simulated Web Contents from {url} (Retries: {retries}, Timeout: {timeout}s)"

fetch_url("https://www.youtube.com/", 4, 6)

quick_fetch = partial(fetch_url, retries=1, timeout=2)

robust_url = partial(fetch_url, retries=5, timeout=30)


print(quick_fetch("https://www.youtube.com/"))
print(robust_url("https://www.youtube.com/"))
print(robust_url("https://www.youtube.com/"))