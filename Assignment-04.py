fruits = {"Apple", "Banana", "Orange", "Mango", "Grapes",
          "Pineapple", "Papaya", "Guava", "Litchi", "Pomegranate"}

summer_fruits = {"Mango", "Litchi", "Watermelon", "Muskmelon", "Jackfruit"}

winter_fruits = {"Apple", "Orange", "Kiwi", "Pear", "Strawberry"}

print("Fruits:", fruits | summer_fruits | winter_fruits)

print("\nFruits present in Fruits and Winter Fruits:")
print(fruits & winter_fruits)

print("\nFruits present only in Summer Fruits but not in Fruits:")
print(summer_fruits - fruits)

print("\nFruits present in Summer and Winter Fruits but not in Fruits:")
print((summer_fruits & winter_fruits) - fruits)

if "Orange" in fruits:
    print("\nOrange is present in Fruits.")
else:
    print("\nOrange is not present in Fruits.")

print("\nPineapple is present in:")

if "Pineapple" in fruits:
    print("Fruits")

if "Pineapple" in summer_fruits:
    print("Summer Fruits")

if "Pineapple" in winter_fruits:
    print("Winter Fruits")