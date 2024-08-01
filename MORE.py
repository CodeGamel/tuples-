library = ("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")


def add_book(author, title):
    title = input("Enter Book: ")
    author = input("Enter Author: ")
    new_book = (title, author,)
    if new_book in library:
        return "Book already exists in the library."
    else:
        str(library)
        new_library = (library) + (new_book,)
        return "Book added successfully."


def view(library):
    print(library)