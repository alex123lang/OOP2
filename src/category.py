class Category:
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
        self.__products.append(item)
        Category.total_quantity += 1

    @property
    def format_products(self):
        product_list = []
        for product in self.__products:
            product_list.append(f"{product.name}, {product.price} руб. Остаток: {product.product_quantity} шт.")
        return product_list

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'
