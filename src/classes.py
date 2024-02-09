class Category:
    name = str
    description = str
    products = list
    category_quantity = int
    total_quantity = int

    def __init__(self, name, description, products, category_quantity, total_quantity):
        self.name = name
        self.description = description
        self.products = products
        self.category_quantity = category_quantity
        self.total_quantity = total_quantity


class Product:
    name = str
    description = str
    price = float
    product_quantity = int

    def __init__(self, name, description, price, product_quantity):
        self.name = name
        self.description = description
        self.price = price
        self.product_quantity = product_quantity
