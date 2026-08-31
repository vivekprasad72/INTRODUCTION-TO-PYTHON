emp = (
    "Ankit", "Rahul", "Sanjeev", "Amit", "Janvi",
    "Rahul", "Rahul", "Ankit", "Karan", "Kaushik",
    "Janvi", "Amit", "Vivek", "Riyanshi", "Sanjeev",
    "Ayashi", "Sumit", "Rahul", "Sanjeev", "Amit"
)

print("Frequencies:")
for name in set(emp):
    print(name, emp.count(name))

names = set(emp)
print("\nDistinct names:", names)
print("Total distinct:", len(names))

print("\nMost frequent:", max(names, key=emp.count))

print("\nSorted:", tuple(sorted(emp)))

name = input("\nEnter name to search: ")
if name in emp:
    print("Found!")
else:
    print("Not found!")