

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

while True:
    print("Add a product")
    print("Type quit to quit program")
    command = input("Type a command")

    if command == "quit":
        break

