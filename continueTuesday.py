""" 
What we learned so far

IMP:
DICT
Sets
Counter
namedtuple
collections in python
Basic operations & checks in sets

"""
from collections import namedtuple
from collections import Counter
from collections import defaultdict

WorkDays = namedtuple("WorkDays", ["day", "work_type"])
gloryDays = {
    "Monday" : "Revision",
    "Tuesday" : "Study + Grind again",
    "Wednesday": "Noe tomorrow"
}

finalWork = [WorkDays(day = k, work_type = v) for k, v in gloryDays.items()]

for records in finalWork:
    print(f"On {records.day}, my work type is {records.work_type}")



#The above example was an example of dictionaries with namedtuple

#let us see a counter example

#custom made counter first

counter = {}

for k, v in gloryDays.items():
    for char in k:
        if char not in counter:
            counter[char] = 0
        counter[char] += 1
    for chars in v:
        if chars not in counter:
            counter[chars] = 0
        counter[chars] += 1

print(counter)

total_chars = 0

for ch in counter:
    total_chars += counter[ch]

print(total_chars)

word_avg = 0
for c in counter:
    word_avg = max(0, counter[c] / total_chars)

    print(f"The average word counts of each character {c} is: {word_avg}")

word_most_frequent = defaultdict(list)

for k, v in counter.items():
    word_most_frequent[k].append(v)

countMaster = Counter(word_most_frequent)

most_frequent = countMaster.most_common(4)

print(most_frequent)

