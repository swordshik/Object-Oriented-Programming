from device import Device 

class Smartphone(Device):

    def __init__(self, name = 'Nothing', price = 0, stock = 0, warranty_period = 1, screen_size = '6.5', battery_size = 0):
        super().__init__(name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.battery_size = battery_size

    def display_info(self):
        return f'Name: {self.name}, Price: {self.get_price()}, Stock: {self.stock}, Warranty period: {self.get_warranty_period()}, Screen size: {self.screen_size}, Battery size: {self.battery_size}'
    
    def set_screen_size(self, screen_size):
        self.screen_size = screen_size
    
    def set_battery_size(self, battery_size):
        self.battery_size = battery_size

    def make_call(self):
        print('Calling...')
        print('Successful call')

    def install_app(self, app_name):
        print(f'Installing {app_name}...')
        print('Installation successful')

    