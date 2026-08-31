import numpy as np

# 2D array of marks
marks = np.array([
    [69, 90, 40],
    [33, 35, 99],
    [45, 58, 95],
    [58, 75, 40],
    [38, 62, 88]
])

# Find Maximum Marks

maximum = np.max(marks)
print("1. Maximum marks:", maximum)

# Find Minimum Marks

minimum = np.min(marks)
print("2. Minimum marks:", minimum)

# Find Average Marks

average = np.mean(marks)
print("3. Average marks:", average)

# Find Maximum Marks Subject-wise

print("4. Maximum marks subject-wise:")

for j in range(3):
    maximum = np.max(marks[:, j])
    print("Subject", j, ":", maximum)

# Find Average Marks Subject-wise

print("5. Average marks subject-wise:")

for j in range(3):
    average = np.mean(marks[:, j])
    print("Subject", j, ":", average)

# Add 10 marks for all students whose Subject 1 score is less than 50

marks[marks[:, 1] < 50, 1] += 10

print("6. Marks after adding 10 to Subject 1:")
print(marks)

# Find number of students whose Subject 2 score is more than 80

count = np.sum(marks[:, 2] > 80)

print("7. Number of students scoring more than 80 in Subject 2:", count)

# Find minimum marks of Student 2

minimum_student2 = np.min(marks[1])

print("8. Minimum marks of Student 2:", minimum_student2)

# Find maximum marks of Student 4

maximum_student4 = np.max(marks[3])

print("9. Maximum marks of Student 4:", maximum_student4)