class Student:
    def __init__(self, name, dept, roll_no):
        self.name = name
        self.dept = dept
        self.roll_no = roll_no

    def show(self):
        print("Name:", self.name)
        print("Department:", self.dept)
        print("Roll No:", self.roll_no)
        print("-------------------")


# Creating 5 student objects
s1 = Student("Rahul", "CSE", 101)
s2 = Student("Rohul", "AIML", 102)
s3 = Student("Ayashi", "ECE", 103)
s4 = Student("Vivek", "AIML", 104)
s5 = Student("Koustav", "CSE", 105)

# Displaying records
s1.show()
s2.show()
s3.show()
s4.show()
s5.show()