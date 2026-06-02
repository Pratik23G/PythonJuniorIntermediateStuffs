""" 
We will continue about generators

"""
import itertools
#note for generators too, you could do things like list comprehension
workload = [12, 34, 568, 457, 67, 90, 123, 442, 444, 556, 679, 976, 654, 543, 532]
result = (row for row in workload if row < 20)

print(result)


#you can use range() for small or limited value lengths

print(range(5))


#to print the infinite length you can use yield like before it comes in handy

def infinite_seq():
    response = 0
    while True:
        yield
        response += 1


outputRes = infinite_seq()
print(next(outputRes))
# print(outputRes)

print(next(outputRes))

print(next(outputRes))


# for i in infinite_seq():
#     print("i : ", i)

def fibonacci():
    number_res = 0
    curr_num = 1
    while True:
        yield number_res
        number_res, curr_num = curr_num, number_res + curr_num
    
print(list(itertools.islice(fibonacci(), 10)))

def take_while_under(gen, limit):
    for num in gen:
        if num <= limit:
            yield num
        else:
            break

print(list(take_while_under(fibonacci(), 100)))