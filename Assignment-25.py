#write a py program to store bookdetail(title,author,year of publication,price) in a variable. now perform the following operations:
#print type of variable
#add 'edition'in the variable
#show the records of 2 books
#show the records of books with lowest price

# Store details of books
books = [
    {
        "title": "Python Programming",
        "author": "John Smith",
        "year": 2022,
        "price": 450
    },
    {
        "title": "Data Science",
        "author": "Robert Brown",
        "year": 2023,
        "price": 550
    }
]

# 1. Print type of variable
print("Type of variable:", type(books))

# 2. Add 'edition' in the variable
for book in books:
    book["edition"] = "1st Edition"

print("\nBook details after adding edition:")
for book in books:
    print(book)

# 3. Show the records of 2 books
print("\nRecords of 2 books:")
for book in books:
    print(book)

# 4. Show the record of book with lowest price
lowest_price_book = min(books, key=lambda book: book["price"])

print("\nBook with lowest price:")
print(lowest_price_book)