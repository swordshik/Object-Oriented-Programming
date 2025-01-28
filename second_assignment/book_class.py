class Book:

    def __init__(self, title=None, author = None, __pages = None, price=None):
        self.title = title
        self.author = author
        self.pages = __pages
        self.price = price

    def display_info(self):
        print("The book", self.title, "by", self.author, "has", self.pages, "pages. It costs", self.price)
    

    def swap_the_prices(self, price1, price2):
        self.price = price1
        price1 = price2
        price2 = self.price
        return [price1, price2]