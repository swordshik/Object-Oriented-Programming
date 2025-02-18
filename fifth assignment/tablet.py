import Device from device

class Tablet(Device):
    def __init__(self, name = 'Nothing', price = 0, stock = 0, warranty_period = 1, screen_resolution = 0, weight = 0):
        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def display_info(self):
        return f'Name: {self.name}, Price: {self.get_price()}, Stock: {self.stock}, Warranty period: {self.get_warranty_period()}, Screen resolution: {self.screen_resolution}, Weight: {self.weight}'
    
    def browse_internet():
        print('Browsing the internet...')
        print('Internet browsing successful')

    def use_touchscreen():
        print('Touching screen...')
        print('Touch screen used')