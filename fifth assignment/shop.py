from laptop import Laptop 
from device import Device 
from tablet import Tablet 
from smartphone import Smartphone

class Shop:
    def __init__(self):
        self.devices = []
        
    def add_device(self, device):
        self.devices.append(device)
        
    def remove_device(self, device):
        self.devices.remove(device)
        
    def display_devices(self):
        for device in self.devices:
            print(device.display_info())
            
    def get_devices(self):
        return self.devices