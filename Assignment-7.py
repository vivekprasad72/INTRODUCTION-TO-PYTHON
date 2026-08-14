text = "Python Programming"

# 1. Display PYTHON
print("1.", text.split()[0])

# 2. Display PROGRAMMING
print("2.", text.split()[1])

# 3. Check JAVA and include it if not present
if "Java" not in text:
    text = text.replace(" ", " Java ")

print("3.", text)

# 4. Length of new string
print("4.", len(text))

# 5. Number of words
print("5.", len(text.split()))

# 6. Capitalize each word
print("6.", text.title())

# 7. Remove all spaces
print("7.", text.replace(" ", ""))

# 8. Frequency of A, P, R, M
print("8.")
print("A =", text.count("A"))
print("P =", text.count("P"))
print("R =", text.count("R"))
print("M =", text.count("M"))