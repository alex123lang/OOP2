from abc import ABC, abstractmethod
from src.mixin import MixinOutput


class Base(ABC):

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def count_products(self):
        pass


class Product(Base, MixinOutput):
    name: str
    description: str
    price: float
    product_quantity: int

    def __init__(self, name, description, price, product_quantity):
        super().__init__()
        self.name = name
        self.description = description
        self.price = price
        self.product_quantity = product_quantity

    def count_products(self):
        return self.product_quantity

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
        if not isinstance(other, type(self)):
            raise TypeError
        return (self.price * self.product_quantity) + (other.price * other.product_quantity)


class Smartphones(Product, MixinOutput):

    efficiency: float
    model: str
    internal_memory: int
    colour: str

    def __init__(self, name, description, price, product_quantity, efficiency, model, internal_memory, colour):
        super().__init__(name, description, price, product_quantity)
        self.efficiency = efficiency
        self.model = model
        self.internal_memory = internal_memory
        self.colour = colour

    def count_products(self):
        return self.product_quantity


class LawnGrass(Product, MixinOutput):

    made_in: str
    germination: int
    colour: str

    def __init__(self, name, description, price, product_quantity, made_in, germination, colour):
        super().__init__(name, description, price, product_quantity)
        self.made_in = made_in
        self.germination = germination
        self.colour = colour

    def count_products(self):
        return self.product_quantity



