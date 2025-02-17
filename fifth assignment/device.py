class Device:

    def __init__(self, name = 'Nothing', price = 0, stock = 0, warranty_period = 1):
        self.name = name
        self.__price = price
        self.stock = stock
        self.__warranty_period = warranty_period

    def display_info(self):
        return f'Name: {self.name}, Price: {self.__price}, Stock: {self.stock}, Warranty period: {self.__warranty_period}'
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price   
    
    def get_warranty_period(self):
        return self.__warranty_period

    def set_warranty_period(self, warranty_period):
        self.__warranty_period = warranty_period
    
    def set_stock(self, stock):
        self.stock = stock

    def reduce_stock(self, amount):
        if self.stock > 0:
            self.stock -= amount
            return self.stock
        else:
            return 'Out of stock'
    
    def is_available(self):
        return self.stock > 0

    def apply_discount(self, discount):
        return self.__price * (1 - (discount)*0.01)