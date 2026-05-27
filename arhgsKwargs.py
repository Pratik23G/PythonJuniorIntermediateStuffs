#args and kwargs seem really cool,
""" 
args - positional arguments
kwargs - keyword arguments

* -> Unpacking operators
** -> Unpacking operators

"""

#good args example

def findSum(*args):
    result = 0
    for val in args:
        result += val
    return result

print(findSum(2, 1, 3))


#kwargs example

def extractVal(**kwargs):
    count = {}
    for k, v in kwargs.items():
        if k not in count:
            count[k] = 0
        count[k] += 1
        if v not in count:
            count[v] = 0
        count[v] += 1
    return count

print(extractVal(Name = "Pratik",
                   City = "Belmont"
                ))

def summarize(*numbers, precision: int = 2):
    if not numbers:
        return {"min": 0.0, "max": 0.0, "avg": 0.0}

    minVal = round(min(numbers), precision)
    maxVal = round(max(numbers), precision)
    average = round(sum(numbers) / len(numbers), precision)
    finalResult = {"min" : minVal, "max": maxVal, "avg" : average}
    return finalResult

print(summarize(0, 1, 2))