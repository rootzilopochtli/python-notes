import my_functions
import os
my_functions.print_options()
option = input()
books = []
while option != 'X' and option != "x":
    # do stuff here
    if option == '1':
        #my_functions.create_book()
        books.append(my_functions.create_book())
        #input("command executed ...press any button")
    elif option == '2':
        my_functions.save_books(books)
    elif option == '3':
        #print(my_functions.load_books())
        books = my_functions.load_books()
    elif option == '4':
        my_functions.issue_book(books)
    elif option == '5':
        my_functions.return_book(books)
    elif option == '6':
        my_functions.update_book(books)
    elif option == '7':
        my_functions.show_all_books(books)
    elif option == '8':
        my_functions.show_book(books)
    else:
        print("The given command doesn't exist..")
    input("Press enter to continue...")
    # asking for input
    os.system("clear")
    my_functions.print_options()
    option = input()
