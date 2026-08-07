marks = [5, 9, 7, 10, 8, 6, 4, 3, 2, 1]
names = ['Aarav', 'Ayashi', 'Karan', 'Juhi', 'Rahul', 'Vivek', 'Kanishk', 'Aditya', 'Emanuel', 'Rohul']

above_8_marks = []
above_8_names = []

for i in range(len(marks)):
    if marks[i] > 8:
        above_8_marks.append(marks[i])
        above_8_names.append(names[i])

print("Original Marks:", marks)
print("Marks > 8:", above_8_marks)
print("Students scoring > 8:", above_8_names)