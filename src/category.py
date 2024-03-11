from src.product import Product
from src.mixin import MixinOutput


class Category(MixinOutput):
    name: str
    description: str
    products: list
    category_quantity: int
    total_quantity: int

    category_quantity = 0
    total_quantity = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_quantity += 1
        Category.total_quantity += len(products)

    @property
    def products(self):
        return self.__products

    def add_product(self, item):
        if isinstance(item, Product):
            if item.product_quantity == 0:
                raise ValueError("Нельзя добавить товар с нулевым количеством!")
            self.__products.append(item)
            Category.total_quantity += 1

    @property
    def format_products(self):
        product_list = []
        for product in self.__products:
            product_list.append(f"{product.name}, {product.price} руб. Остаток: {product.product_quantity} шт.")
        return product_list

    def average_price(self):
        try:
            total_price = sum(product.price for product in self.__products)
            average_price = total_price / sum(product.product_quantity for product in self.__products)
            return average_price
        except ZeroDivisionError:
            return 0

    def __len__(self):
        return sum(product.product_quantity for product in self.__products)

    def __str__(self):
        total_count = sum(product.product_quantity for product in self.__products)
        return f'{self.name}, количество продуктов: {total_count} шт.'
