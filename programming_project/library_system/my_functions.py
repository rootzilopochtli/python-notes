from book import Book
import json

# print options
def print_options():
    print("Press the specific button for that action")
    print("1-Create a new book")
    print("2-Save books locally")
    print("3-Load books from the disk")
    print("4-Issue book")
    print("5-Return a book")
    print("6-Update a book")
    print("7-Show all books")
    print("8-Show book")

# create_book_function
def input_book_info():
    id = input("ID: ")
    name = input("Name: ")
    description = input("Description: ")
    isbn = input("ISBN: ")
    page_count = int(input("Page Count: "))
    issued = input("Issued: y/Y for True, anything else for False ")
    issued = (issued == "y" or issued == "Y")
    author = input("Author Name: ")
    year = int(input("Year: "))
    return{
        'id' : id,
        'name' : name,
        'description' : description,
        'isbn' : isbn,
        'page_count' : page_count,
        'issued' : issued,
        'author' : author,
        'year' : year
    }


def create_book():
    print("Please enter your book information")
    book_input = input_book_info()
    book = Book(book_input['id'], book_input['name'], book_input['description'], book_input['isbn'],
                book_input['page_count'], book_input['issued'], book_input['author'], book_input['year'])
    print(book.to_dict())
    return book
    # book = Book("")

# defining save_books
def save_books(books):
    json_books = []
    for book in books:
        json_books.append(book.to_dict())
    try:
        file = open("books.dat", "w")
        file.write(json.dumps(json_books, indent = 4))
    except:
        print("We had an error saving books")

def load_books():
    try:
        file = open("books.dat", "r")
        loaded_books = json.loads(file.read())
        books = []
        for book in loaded_books:
            new_obj = Book(book['id'], book['name'], book['description'], book['isbn'],
                           book['page_count'], book['issued'], book['author'], book['year'])
            books.append(new_obj)
        print("Successfully loaded books")
        return books
    except:
        print("The file doesn't exist or an error ocurred during loading")

# find book function..
# takes books and id
# if found returns the index of book in the books array, if not returns nothing
def find_book(books, id):
    for index, book in enumerate(books):
        if book.id == id:
            return index
    return None

# issue book
# asks the user for the id input
# then finds the id of the book we are looking for
# sets the value of issued to true for that book
def issue_book(books):
    id = input("Enter the id of the book you want to issue: ")
    index = find_book(books, id)
    if index != None:
        books[index].issued = True
        print("Book successfully issued")
    else:
        print("Could not find the book you are looking for")

# return books
def return_book(books):
    id = input("Enter the id of the book you want to return: ")
    index = find_book(books, id)
    if index != None:
        books[index].issued = False
        print("Book successfully returned")
    else:
        print("Could not find the book you are looking for")

# update book function
# in the function parameter it takes books
# first it asks for the id input
# finds the book id
# if the book found... creates a new book using already writen function
# the book is replaced with this book
# if book not found, we just say its not found
def update_book(books):
    id = input("Enter the ID of book you want to update: ")
    index = find_book(books, id)
    if index != None:
        new_book = create_book()
        old_book = books[index]
        books[index] = new_book
        del old_book
        print("Book successfully updated")
    else:
        print("Could not find your book")

# show all books
# show book
def show_all_books(books):
    for book in books:
        print(book.to_dict())

def show_book(books):
    id = input("Enter the ID of book you're looking for: ")
    index = find_book(books, id)
    if index != None:
        print(books[index].to_dict())
    else:
        print("Could not find your book")
