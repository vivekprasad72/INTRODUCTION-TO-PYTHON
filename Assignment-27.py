#create class product with product_id,poll-name,quantity
#initialize with constructor
#show() method to display the records
#create 2 objects p1,p2 and show the details.

# Create a Product class
class Product:

    # Constructor
    def __init__(self, product_id, product_name, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity

    # show() method
    def show(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Quantity:", self.quantity)


# Create two objects
p1 = Product(101, "Laptop", 5)
p2 = Product(102, "Mobile", 10)

# Display details
print("Product 1 Details:")
p1.show()

print("\nProduct 2 Details:")
p2.show()