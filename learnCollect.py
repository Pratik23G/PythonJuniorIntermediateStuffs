#creating your own subclass requires to know 2 things
""" 
typename: Name of your class we are making

field_names: list of names we will use to access in resulting tuple
    Criterias -----:
    1) iterable of strings like ["f1", "f2", ...., "fn"]
    2) string with whitespace-separated field names as "field1 filed2 ... fieldN"
    3) String with comma spearated filed names like "f1, f2, ... fn"

"""

#example:
from collections import namedtuple
from collections import Counter
from collections import defaultdict

Points = namedtuple("Points", ["A", "B"])
grades = Points(90, 85)

print(grades)

GroceryList = namedtuple("GroceryList", "apple, Paneer, Potato, Zuchini, Salmon, Chicken")
item_list = GroceryList("fruits", "protein", "carbs", "salad", "healthy", "high protein")

print(item_list)

#we can also count number of occurances of objects in a list at once

word = "hellohelloworldhelloworld"

counter = {}

for letter in word:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1

print(counter)

counted_val = Counter("MessiMessiTheGoat")
print(counted_val)


""" 
Note: A subtle thing to know although counter is a subclass of 
dictionary it does not have feature of fromkeys() to set all values to be same
for the items, but it does use .update which adds on top of the existing values
"""

letters = Counter("mississippi")

letters.update(m = 3, i = 4)

print(letters)

letters = Counter("mississppi")
letters["a"]

inventory = Counter(dogs = 23, cats = 14, pythons = 7)

adopted = Counter(dogs = 2, cats = 5, pythons = 1)
inventory.subtract(adopted)
print(inventory)

orders = [
    ("alice", "book"), ("bob", "pen"), ("alice", "pen"),
    ("carol", "book"), ("bob", "book"), ("alice", "book"),
    ("carol", "notebook"), ("bob", "book"),
]

dataLog = defaultdict(list)

for k, v in orders:
    dataLog[k].append(v)
       

print(dataLog)

dataFed = [item for subList in dataLog.values() for item in subList]

bigCountData = Counter(dataFed)

topTwoProducts = bigCountData.most_common(2)

print(topTwoProducts)
