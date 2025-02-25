from laptop import Laptop 
from device import Device 
from tablet import Tablet 
from smartphone import Smartphone
from cart import Cart
from shop import Shop
from time import sleep

cart = Cart()
shop = Shop()

laptop1 = Laptop('Dell XPS 13', 2000, 10, '3 months', 16, 512)
laptop2 = Laptop('MacBook Pro', 2500, 5, '24 months', 32, 1024)
tablet1 = Tablet('iPad Pro', 1000, 20, '18 months', 6, 128)
tablet2 = Tablet('Samsung Galaxy Tab S7', 800, 15, '12 months', 8, 256)
smartphone1 = Smartphone('iPhone 12', 1200, 30, '18 months', '5.7', 5000)
smartphone2 = Smartphone('Samsung Galaxy S21', 1000, 25, '9 months', '6', 4500)

shop.add_device(laptop1)
shop.add_device(laptop2)
shop.add_device(tablet1)
shop.add_device(tablet2)
shop.add_device(smartphone1)
shop.add_device(smartphone2)

def find_device_by_name(name):
    for device in shop.devices:
        if device.name == name:
            return device
    return None

def main():
    while True:
        print('Menu')
        print('1. Display devices')
        print('2. Add device to cart')
        print('3. Remove device from cart')
        print('4. Display cart')
        print('5. Calculate total price')
        print('6. Apply discount')
        print('7. Checkout')
        print('8. Exit')
        choice = int(input('Enter your choice: '))
        
        if choice == 1:
            shop.display_devices()
            sleep(4)
        elif choice == 2:
            device_name = input('Enter device name: ')
            device = find_device_by_name(device_name)
            if device:
                amount = int(input('Enter amount: '))
                cart.add_device(device, amount)
                print('Device added to cart')
            else:
                print('Device not found')
            sleep(4)
        elif choice == 3:
            device_name = input('Enter device name: ')
            device = find_device_by_name(device_name)
            if device:
                cart.remove_device(device)
                print('Device removed from cart')
            else:
                print('Device not found')
            sleep(4)
        elif choice == 4:
            if len(cart.get_cart()) == 0:
                print('Cart is empty')
            else:
                cart.display_info()
            sleep(4)
        elif choice == 5:
            print(f'Total price: {cart.calculate_total_price()}')
            sleep(4)
        elif choice == 6:
            discount = int(input('Enter discount percentage: '))
            print(f'Total price after discount: {cart.apply_discount(discount)}')
            sleep(4)
        elif choice == 7:
            cart.checkout()
            sleep(4)
        elif choice == 8:
            break
        else:
            print('Invalid choice')
            sleep(2)

main()