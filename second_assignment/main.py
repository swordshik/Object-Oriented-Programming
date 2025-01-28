from book_class import Book

if __name__  == "__main__":
    objects = []

    # Create some book instances
    book1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
    book2 = Book("War and Peace", "Lev Tolstoy", 1225, 39.95)
    book3 = Book("The Catcher in the Rye", "JD Salinger", 234, 24.95)

    objects = objects + [book1, book2, book3]

    # Call the book_info method for each book
    for i in objects:
        i.display_info()

    # Call the swap_the_prices method for each book
    objects[0].price=objects[0].swap_the_prices(objects[0].price, objects[1].price)[0]

    print("\nAfter swapping the prices of the first two books:")  
    objects[0].display_info()