from src.category import Category
from src.product import Product


def test_category():
    category = Category("test", "test description", ['product 1', 'product 2'])
    assert category.name == "test"
    assert category.description == "test description"
    assert category.products == ['product 1', 'product 2']
    assert Category.category_quantity == 1
    assert Category.total_quantity == 2


def test_product():
    product = Product("test", "test description", 10_000, 5)
    assert product.name == "test"
    assert product.description == "test description"
    assert product.price == 10_000
    assert product.product_quantity == 5

