# 20 employee names
emp = (
    "Ankit", "Rahul", "Sanjeev", "Amit", "Janvi",
    "Rahul", "Rahul", "Ankit", "Karan", "Kaushik",
    "Janvi", "Amit", "Vivek", "Riyanshi", "Sanjeev",
    "Ayashi", "Sumit", "Rahul", "Sanjeev", "Amit"
)

# i) Name and frequency
print("Frequencies:")
for name in set(emp):
    print(name, emp.count(name))

# ii) Distinct names
names = set(emp)
print("\nDistinct names:", names)
print("Total distinct:", len(names))

# iii) Most frequent employee
print("\nMost frequent:", max(names, key=emp.count))

# iv) Sorted tuple
print("\nSorted:", tuple(sorted(emp)))

# v) Search employee
name = input("\nEnter name to search: ")
if name in emp:
    print("Found!")
else:
    print("Not found!")