#yesterday we did some cool stuffs with dicts and collections

""" 
Recap:

We learned how to do list comprehension with for loops
use default-dicts, use namedtuples and Counter(), built in library for python

 """
#imports from Python Library:
from collections import Counter
from collections import namedtuple

#some examples:
#python dicts created VS default dicts

humanEvol = {
    "Apes" : "Ancient",
    "Homosaphians": "Former evolution Gorilla-Man",
    "Caveman" : "First form",
    "Indegenious" : "reformations",
    "Modern" : "Humans",
}

#default dict() library with (mapping, **kwargs)

updatedEvol = dict(humanEvol, future = "Aliens")

print(humanEvol)
print(updatedEvol)

#Use of user made counter VS default counter

counter = {}
wordM = "Missoula"
for letter in wordM:
    if letter not in counter:
        counter[letter] = 0
    counter[letter] += 1

print(counter)


#Counter() -> Built in same feature in Python

masterC = Counter(wordM)
print(masterC)

#making your own subtuples using namedtuple classic python way
Informatics = namedtuple("Informatics", ["Evolution", "Type"])

#this is where we use list comprehension
results = tuple(Informatics(k, v) for k, v in humanEvol.items())

format = ",".join([f"(Evolution = {i.Evolution} , Type = {i.Type})" for i in results])

print(format)

""" 
Agenda for today:

Sets & some examples

 """
#simple example of sets, as they are mutable, hashable and unique
# + unordered 

#3 ways to create sets:
#1.1 - Use set literals
userNum = {23, 22, 21, 20}

# uniqueNum = set(userNum)
print(userNum)

#1.2 Use set() python predefined library constructor

language = "Python"
numLang = set(language)
print(numLang)

#1.3 String Comprehensions
#syntax {expr for expr in some iterables [if condition]<-This part is optional}

studentScores = {"Ryan": 67,
                "Miles": 90,
                "Pratik": 86,
                "Peter": 96,
}

resultScore = {score for score in studentScores.values()}
print(resultScore)

#Now time for basic set operations
#Unions

weather = {"Sunny", "Windy", "Foggy", "HalfMoon-Bay"}

cities = {"San Mateo", "Daly City", "HalfMoon-Bay"}

foodStops = {"Zareens", "Uzami Ramen", "Himalayan Monsoon Bay", "San Mateo"}

print(cities | foodStops)


combinedResult = weather.union(cities)
print(combinedResult)

#Note you can't use list + sets for union it will give type error
# as union does not support different types of sets

#lets so some INtersections !!!!!
ultimateIntersect = weather.intersection(cities)
print(cities & foodStops)
#also does the same thing

#we will now talk about subsets, proper set, super set, proper subsets,
#and proper supersets

schoolCoverage = {3, 4, 5, 6}
sampleSpace = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(schoolCoverage.issubset(sampleSpace)) #gives true
#also can be written as this
print(schoolCoverage <= sampleSpace)

print(sampleSpace.issuperset(schoolCoverage)) #gives true b/c sampleSpace has all stuffs found inside schoolCoverage

#can also be written as
print(sampleSpace >= schoolCoverage)

#Proper subsets & supersets
#same idealogy but one strictly is subset and other is a superset without having 
#eqaulity property

print(sampleSpace > schoolCoverage)

print(schoolCoverage < sampleSpace)
