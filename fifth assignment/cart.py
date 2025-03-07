class Cart:
    def __init__(self):
        self.cart = []
        
    def add_device(self, device, amount):
        tuple = (device, amount)
        self.cart.append(tuple)
        
    def remove_device(self, device):
        self.cart = [item for item in self.cart if item[0] != device]
        
    def calculate_total_price(self):
        total_price = 0
        for device, amount in self.cart:
            total_price += device.get_price() * amount
        return total_price
    
    def apply_discount(self, discount):
        total_price = self.calculate_total_price()
        return total_price * (1 - discount * 0.01)
    
    def display_info(self):
        for device, amount in self.cart:
            print(device.display_info())
    
    def checkout(self):
        for device, amount in self.cart:
            if device.is_available():
                device.reduce_stock(amount)
            else:
                print(f'{device.name} is out of stock')
        self.cart = []
        print('Checkout successful')
        
    def get_cart(self):
        return self.cart