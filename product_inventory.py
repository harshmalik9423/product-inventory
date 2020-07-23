from json import dumps, loads

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_dict(self):
        return { 'name': self.name, 'price': self.price }

def load_products():
    products_file = open("products.json", "r+")
    product_json = products_file.read()
    product_data = loads(product_json)
    products = []
    for product in product_data:
        products.append(Product(product['name'], product['price']))
    products_file.close()
    return products

def add_product(name, price):
    new_product = Product(name,price)
    products.append(new_product)

def list_products(products):
    for p in products:
        print("Product : " + p.name + " and Price : " + str(p.price))

def save_products(products):
    products_save_list = []
    for product in products:
        products_save_list.append(product.to_dict())
    
    products_file = open("products.json", "w+")
    products_file.write(dumps(products_save_list))
    products_file.close()

products = load_products()
while True:
    print("Type 'add' to add a product")
    print("Type 'quit' to quit program")
    print("Type 'list' to list all products")
    command = input("Type a command: ")

    if command == "quit":
        save_products(products)
        break
    
    if command == "add":
        product_name = input("Enter name of the product : ")
        product_price = float(input("Enter the price : "))
        add_product(product_name, product_price)

    elif command == "list":
        list_products(products)
