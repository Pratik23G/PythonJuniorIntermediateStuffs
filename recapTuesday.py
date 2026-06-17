#recap quickly from yesterday

#lru_cache from functools, Least Recently used cache eviction policy
#saves storage unlike cached_memory which has unlimited size

from functools import lru_cache, partial, reduce

@lru_cache(maxsize=128)
def fact(n):
    print(f"Calculating factorial of {n}")
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)


def multNum(userNum, exp):
    return userNum ** exp

funCube = partial(multNum, exp=3)
funSq = partial(multNum, exp=2)

numberAdd = reduce(lambda acc, n: acc + n, [1, 2 ,4 ,1], 0)

print(fact(3))
print(fact(3))

print(funCube(2))
print(funSq(3))

print(numberAdd)