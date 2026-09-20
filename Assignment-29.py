#create two sets of product names that one bought during july & august 
#find the product name that is bought only in july
#find the product that one bought in both month
#find the total product that one bought in july & august.

# Create two sets of products
july = {"Laptop", "Mobile", "Headphones", "Mouse"}
august = {"Mobile", "Keyboard", "Headphones", "Charger"}

# 1. Products bought only in July
only_july = july - august
print("Products bought only in July:", only_july)

# 2. Products bought in both July and August
both_months = july & august
print("Products bought in both months:", both_months)

# 3. Total unique products bought in July and August
total_products = july | august
print("Total products bought:", total_products)
print("Total number of unique products:", len(total_products))