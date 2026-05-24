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
Points = namedtuple("Points", ["A", "B"])
grades = Points(90, 85)

print(grades)

GroceryList = namedtuple("GroceryList", "apple, Paneer, Potato, Zuchini, Salmon, Chicken")
item_list = GroceryList("fruits", "protein", "carbs", "salad", "healthy", "high protein")

print(item_list)