#define a class animal with attribute type.
#define a class wild-animal which is child of animal with attributr sound,color.
# define a class pet-animal which is child of animal with attribute food,category.
# intialize all variables with constructor .
# create one object of each child class use show()method to display the record of both animal. 

# Parent class
class Animal:
    def __init__(self, type):
        self.type = type


# Child class of Animal
class WildAnimal(Animal):
    def __init__(self, type, sound, color):
        super().__init__(type)
        self.sound = sound
        self.color = color

    def show(self):
        print("Type:", self.type)
        print("Sound:", self.sound)
        print("Color:", self.color)


# Child class of Animal
class PetAnimal(Animal):
    def __init__(self, type, food, category):
        super().__init__(type)
        self.food = food
        self.category = category

    def show(self):
        print("Type:", self.type)
        print("Food:", self.food)
        print("Category:", self.category)


# Create objects
w1 = WildAnimal("Lion", "Roar", "Brown")
p1 = PetAnimal("Dog", "Dog Food", "Domestic")

# Display records
print("Wild Animal Details:")
w1.show()

print("\nPet Animal Details:")
p1.show()