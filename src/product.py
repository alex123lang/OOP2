class Product:
    name: str
    description: str
    price: float
    product_quantity: int

    def __init__(self, name, description, price, product_quantity):
        self.name = name
        self.description = description
        self.price = price
        self.product_quantity = product_quantity
