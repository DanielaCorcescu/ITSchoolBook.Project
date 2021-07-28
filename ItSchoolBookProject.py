def add_book():
    book_name = input("Insert a book name ->")
    author_name = input("Insert a author name ->")
    # imporint csv lib
    import csv
    with open('booksDB.csv', mode='a+') as file:
        writer = csv.DictWriter(file, fieldnames=[
            "BookName", "AuthorName", "SharedWith", "IsRead"
        ])
        writer.writerow({"BookName": book_name,
                         "AuthorName": author_name,
                         "SharedWith": 'None',
                         "IsRead": False}
                        )
    print("Book was added successfully")


def list_books():
    import csv
    with open('booksDB.csv', mode='r') as file:
        #  pasul 1 sa luam toate datele din DB
        rows = csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead"))
        # parcurgem rand cu rand
        for row in rows:
            print(
                f"Book name is: {row.get('BookName')} Author Name {row.get('AuthorName')} is shared {row.get('ShareWith')} is read  {row.get('IsRead', False)}")


def update_book():
    book_name = input("Enter book name: ")
    book_read = input("Is the book read?(Y/N)?")
    test_update = False
    if book_read == 'Y':
        test_update = True
    else:
        test_update = False
    import csv
    rows = []
    with open('booksDB.csv', mode='r') as file:
        #rows = list(csv.DictReader(file))
        rows = list(csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead")))
        for row in rows:
            if row["BookName"] == book_name:
                row["IsRead"] = test_update
                break
        with open('booksDB.csv', mode='w') as file:
            csv_writer = csv.DictWriter(file, fieldnames=[
                "BookName", "AuthorName", "SharedWith", "IsRead"
            ])
            for row in rows:
                csv_writer.writerow({"BookName": row.get("BookName"),
                                 "AuthorName": row.get("AuthorName"),
                                 "SharedWith": row.get("SharedWith"),
                                 "IsRead": row.get("IsRead")}
                                )
        print("Book was updated successfully")



def share_book():
    book_name= input("What is the name of the book you want to share-> ")
    shared_with = input("With who do you want to share? -> ")

    import csv
    with open('booksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead")))
        for row in rows:
            if row["BookName"] == book_name:
               row["SharedWith"] = shared_with
               break
            else:
                print("Book is not in DB")
        with open('booksDB.csv', mode='a+') as file:
            csv_writer = csv.DictWriter(file, fieldnames=[
            "BookName", "AuthorName", "SharedWith", "IsRead"
            ])
            csv_writer.writerow({"BookName": row.get("BookName"),
                             "AuthorName": row.get("AuthorName"),
                             "SharedWith": shared_with,
                             "IsRead": row.get("IsRead")}
                            )


# Maine menu for user
if __name__ == "__main__":
    while True:
        print("Menu : ")
        print("1 : Add a book")
        print("2 : List books")
        print("3 : Update book")
        print("4 : Share book")
        option = int(input("Select one option -> "))

        if option == 1:
            add_book()
        elif option == 2:
            list_books()
        elif option == 3:
            update_book()
        elif option == 4:
            share_book()
        else:
            print("Not a valid option")


