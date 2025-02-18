import Device from device

class Laptop(Device):
    def __init__(self, name = 'Nothing', price = 0, stock = 0, warranty_period = 1, ram_size = 0, processor_speed = 0):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.processor_speed = processor_speed
        
    def display_info(self):
        return f'Name: {self.name}, Price: {self.get_price()}, Stock: {self.stock}, Warranty period: {self.get_warranty_period()}, RAM size: {self.ram_size}, Processor speed: {self.processor_speed}'
    
    def run_program(program_name):
        print(f'Running {program_name}...')
        print('Program is running')

    def use_keyboard():
        typed = input('Typing:')
        print('Text entered: ', typed)