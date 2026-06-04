#------------Today's imports -----------------#
import dis

#recap on what we learned yesterday

#iterators are actually cool i do noot know much but here is
#what i remember
list_of_num = [23, 45, 67, 78, 90]
next_sum = iter(list_of_num)
print(list(next_sum))


#generators are really good if we have a large data sets to open and read
#they work lazily but saves a lot of memory
#way to open and read the file contents is by using yield

def read_file(file_name):
    with open(file_name, "r") as file:
        for row in file:
            col = row.split("|")
            if len(col) < 4:
                continue

            Offer = col[2].strip()
            Accepted = col[3].strip()
            company_name = col[0].strip()
            if Offer == "Yes" and Accepted == "Yes":
                yield company_name

show_content = read_file("jobGoals.txt")
print(list(show_content))

""" 
We will learn about Lambda functions in python

Lambda function made by Alonzo Church as part of Lambda calculus
works like regular function but has properties like
Beta reduction, alpha substitution etc.

 """

 #regular function

def get_me_val(x):
    return x


print(get_me_val(5))


#lambda function

value_found = lambda x: x #this also works the same

print(value_found(5))

## some more examples now a bit complex

high_order_function = lambda x, func: x + func(x)
print(high_order_function(2, lambda x: x * x))

""" 
the above code snippet works in beta -reduction we first set up
high-order function lambda 2, func: 2 + func(2) --- this func(2)
is wall now as we cannot compute unless we know what that func(2)
is, so we just operate and finf out in the next line which is 
lambda x: x*x this has the same layout as the first previous line
so func(2) = 2 * 2 = 4 returns this to prev line 2 + 4 = 6 is finally
printed

 """

#use of disassemble import method here
add = lambda x, y: x + y
type(add)

dis.dis(add)

def add_vals(x, y):
    return x + y

type(add_vals)

dis.dis(add_vals)

""" 
Some pros of Lambda functions

They can be Immediately Invoked Function Execution (IIFE)
Note this is only good for high order functions like
map(), filter(), functools.reduce() or a key function


            BUT!!!!!
Unlike regular functions hwere we can fo type hinting,
lambda function returns error

ex:
def my_stats(score:int, final_grade: int) -> int:
    return f' {score.user()} {final_grade.user()} ----> GOOD

lambda score:int, final_grades:int -> int -----> \/----> BAD

 """

#lambda arguments
#like regular functions the argument rules are same for lambda functions

result_val = print((lambda x, y, z : x + y + z) (1, 2 ,3))

res_val2 = print((lambda *args: sum(args)) (1, 2, 3))

dicts_val = print((lambda **kwargs: sum(kwargs.values())) (one = 1, two = 2, three = 3))


#decorators simply put is a cool way to wrap some extra function around the original
#function, allowing user to change features without changing any source code

def wrap_this(f):
    def check_id(*args):
        if args[0] < 21:
            print(f"You are under age. Calling! {f.__name__}")
        else:
            print(f"You are good to go. {f.__name__}")
    return check_id

@wrap_this

def body_guard(x):
    print(f"Can i see your Id?", {x})

body_guard(34)
print("-" * 26)


body_guard(18)

#another example with reg function and lambda function

def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)
    return wrap

@trace
def add_two(x):
    return x + 2

print(add_two(3))

print((trace(lambda x: x**2))(3))

