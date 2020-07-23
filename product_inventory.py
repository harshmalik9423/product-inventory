

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

def add_product(name, price):
    new_product = Product(name,price)
    products.append(new_product)

def list_products(products):
    for p in products:
        print("Product : " + p.name + " and Price : " + str(p.price))

products = []
while True:
    print("Type 'add' to add a product")
    print("Type 'quit' to quit program")
    print("Type 'list' to list all products")
    command = input("Type a command: ")

    if command == "quit":
        break
    
    if command == "add":
        product_name = input("Enter name of the product : ")
        product_price = float(input("Enter the price : "))
        add_product(product_name, product_price)

    elif command == "list":
        list_products(products)
