import Device from device

class Smartphone(Device):

    def __init__(self, name = 'Nothing', price = 0, stock = 0, warranty_period = 1, screen_size = 0, camera_resolution = 0):
        super().__init__(name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.camera_resolution = camera_resolution

    def display_info(self):
        return f'Name: {self.name}, Price: {self.get_price()}, Stock: {self.stock}, Warranty period: {self.get_warranty_period()}, Screen size: {self.screen_size}, Camera resolution: {self.camera_resolution}'
    
    def set_screen_size(self, screen_size):
        self.screen_size = screen_size
    
    def set_camera_resolution(self, camera_resolution):
        self.camera_resolution = camera_resolution