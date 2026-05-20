books =[
    "Python Basics",
    "Data Structures",
    "Machine Learning",
    "Web Development",
]

books.append("Artificial Intelligence")

print("Book in library:")
for book in books:
    print("yes is AI",book)


books.remove("Data Structures")

print("\nAtfer Borrowing:")
for book in books:
    print("yes is remove",book)


search = "Python Basics"

if search in books:
    print("\nBook Found")
else:
    print("\nBook Not Found")