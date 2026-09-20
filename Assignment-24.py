#write a python program to take inputa string. now do the following operations on the string:
#1. convert all in lowercase.
#2. convert the string in uppercase.
#3. count the number of characters.
#4. count the number of vowels.

# Take input string
string = input("Enter a string: ")

# 1. Convert to lowercase
print("Lowercase:", string.lower())

# 2. Convert to uppercase
print("Uppercase:", string.upper())

# 3. Count number of characters
print("Number of characters:", len(string))

# 4. Count number of vowels
vowels = "aeiouAEIOU"
count = 0

for ch in string:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)