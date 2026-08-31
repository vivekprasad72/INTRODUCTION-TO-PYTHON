student = {
    101: {"name": "Rahul", "department": "AIML", "marks": 85},
    102: {"name": "Vivek", "department": "AIML", "marks": 92},
    103: {"name": "Ayashi", "department": "AIML", "marks": 78},
    104: {"name": "Rohul", "department": "AIML", "marks": 95},
    105: {"name": "Pinaki", "department": "AIML", "marks": 88}
}

# 1. Sort according to marks (highest to lowest)
sorted_students = dict(
    sorted(student.items(), key=lambda x: x[1]["marks"], reverse=True)
)

print("Students sorted by marks:")
print(sorted_students)


# 2. Print the record of student with maximum marks
maximum = max(student.items(), key=lambda x: x[1]["marks"])

print("\nStudent with maximum marks:")
print(maximum)


# 3. Find average marks
average = sum(map(lambda x: x["marks"], student.values())) / len(student)

print("\nAverage marks:", average)


# 4. Print students scoring more than average
above_average = dict(
    filter(lambda x: x[1]["marks"] > average, student.items())
)

print("\nStudents scoring more than average:")
print(above_average)