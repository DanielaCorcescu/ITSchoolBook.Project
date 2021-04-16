def AddBook():
    book_name = input("Insert a book name ->")
    author_name = input("Insert a author name ->")
    #impor int csv lib
    import csv
    with open('bookDB.csv','w') as file:
        writer = csv.DictWriter(file,fieldnames=[
            "BookName", "AuthorName", "ShareWith", "IsRead"
        ])
        writer.writerow({"BookName": book_name,
                         "AuthorName": author_name})
    print("Book was added successfully")


def ListBook():
    print("List books option")
def UpdateBook():
    print("Update a book option")
def ShareBook():
    print("Share a book option")

# Maine menu for user
print("Meniu : ")
print("1 : Add a book" )
print("2 : List books" )
print("3 : Update book")
print("4 : Share book")
option = int(input("Select one option -> "))


if option == 1:
    AddBook()
elif option == 2:
    ListBook()
elif option == 3:
    UpdateBook()
elif option == 4:
    ShareBook()
else:
    print("Not a valid option")