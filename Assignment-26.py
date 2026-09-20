#write a program using tuple to store the names of 5 cities
#print all items
#print 1st 2 cities
#print city that present twice in the tuple


# Store names of 5 cities in a tuple
cities = ("Kolkata", "Delhi", "Mumbai", "Kolkata", "Chennai")

# 1. Print all items
print("All cities:")
for city in cities:
    print(city)

# 2. Print first 2 cities
print("\nFirst 2 cities:")
print(cities[:2])

# 3. Print city that is present twice
print("\nCity present twice:")
for city in cities:
    if cities.count(city) == 2:
        print(city)
        break