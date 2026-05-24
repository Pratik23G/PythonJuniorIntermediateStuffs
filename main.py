print("hello we will add more stuffs later in next 15-20 mins")

userRepo ={
    "name": "Pratik23G",
    "project": "Junior Python role",
    "target_days": 14,
}

userRepo["email"] = "pratikgurung022@gmail.com"

print(userRepo.get("phone", "n/a"))

print(userRepo)

view = list(userRepo.keys()), list(userRepo.values())

print(view)

#now we will learn about colletcions 
""" 
particlaulry named tuples, it helps to create sub class for
tuples with named fields. This field also 
gives users direct access to named tuples using the dot notation
"""

print(divmod(12, 6))
#the above code divmod is classic python division for integer offering the quotient
# and remainder but we don't know whats what there is very less readability
#so we use named tuples to define what each parts or sub tuples are for
#divmod !!!

#NOTE THIS CODE should be on top of the file always for easness i have it here
from collections import namedtuple
#BTW  collections are specialized containers in python librrary which makes coding really
#efficient

def custom_divmod(x, y):
    Divmod = namedtuple("Divmod", "quotient remainder")
    return Divmod(*divmod(x, y))

test_result = custom_divmod(12, 6)
print(test_result)

#TOMORROW: GO MORE IN DEPTH WITH DICTONARIES AND COLLECTIONS FINISH DAY1 TASK

#lists dictionaries and sets can't be used for keys
#b/c they are mutable so we can prefer to use tuples as they are immutable

houseCoordinates = {
    (2, 12) : "X-coordinates",
    (23, 456) : "Y-coordinates",
    (90, 456) : "Z-coordinates"
}

print(houseCoordinates[(2, 12)])

target = "X-coordinates"

keys = [k for k,v in houseCoordinates.items() if v == target]

print(keys)

#we can also build dictionaries values using any type of objects even
# a class

class SampleAge:
    def __iniit__(self, x, y):
        self.x = x,
        self.y = y

outResult = {
    "ph-Scale" : 7.0,
    "timeout" : 3,
    "SampleAge" : (34, 90)
}

print(outResult["SampleAge"])

#you can also use dictionaries dict() method

#dict(): empty {}

ud_id = dict()

print(ud_id)

#dict(**kwargs) : key = value type format, but you can type
# names here no need of quotes for keys

number_one = dict(Messi = 10, Ronaldo = 7)
print(number_one)


#dict(mapping, **kwargs): just another dictionary, takes one dictionary
#adds it to another dictionary to build a new dictionary

example_fact = dict(guess = "wrong", survival = "true")

new_fact = dict(example_fact, survival_rate = 95)

print(new_fact)

#dict(iterable, **kwargs):Pair List
#to build a list must contain pairs like(tuples), good for spreadsheet data

future_stats = [("broke", "no job"), ("grind hard", "guaranteed placement")]

join_forge = dict(future_stats, skills = "working i will get better everyday")

print(join_forge)


#we can also create dictionaries using  built in zip function to
#call zip

cities = [
    "Boston", 
    "NewYork",
    "California",
    "Colorado",
    "Miami",
]

person = [
    "Tom",
    "Sally",
    "Raj",
    "Vinny",
    "Heather",
]

combined = dict(zip(person, cities))
print(combined)

#you can also create dictionaries witj default values using .fromkeys()

inventory = dict.fromkeys(["apple", "Chicken", "Cauliflower"], 0)
print(inventory)