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
        self.products = products
        self.category_quantity = 0
        self.total_quantity = 0

        Category.category_quantity += 1
        Category.total_quantity += len(products)
