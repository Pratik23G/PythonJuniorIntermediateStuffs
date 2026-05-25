import statistics
from collections import defaultdict
students = [
{"name": "Alice", "grades": [88, 92, 79]},
{"name": "Bob", "grades": [70, 65, 80]},
{"name": "Carol", "grades": [95, 91, 100]},
]

#TODO: BUILD a dict mapping name -> average grades



averageScoreDict = {s["name"]: sum(s["grades"]) / len(s["grades"]) for s in students}
print(averageScoreDict)

uniqueGrades = {grades for s in students for grades in s["grades"]}
print(uniqueGrades)

newStudentList = [s["name"] for s in students if (statistics.mean(s["grades"])) >= 85]
print(newStudentList)