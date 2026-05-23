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