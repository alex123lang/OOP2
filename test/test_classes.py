from src.classes import Category, Product


def test_category():
    category = Category("test", "test", [], 0, 0)
    assert category.name == "test"
    assert category.description == "test"
    assert category.products == []
    assert category.category_quantity == 0
    assert category.total_quantity == 0


def test_product():
    product = Product("test", "test", 0, 0)
    assert product.name == "test"
    assert product.description == "test"
    assert product.price == 0
    assert product.product_quantity == 0

