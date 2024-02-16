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

    @staticmethod
    def create_product(name, description, price, product_quantity):
        return Product(name, description, price, product_quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена введена некорректно")
        else:
            self._price = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.product_quantity} шт."

    def __add__(self, other):
        return (self.price * self.product_quantity) + (other.price * other.product_quantity)
