import pytest

from src.category import *
from src.product import *


def test_category():
    product1 = Product("test1", "test description1", 10_000, 5)
    product2 = Product("test2", "test description2", 5_000, 10)
    products = [product1, product2]
    category = Category("test", "test description", products)
    assert category.name == "test"
    assert category.description == "test description"
    assert category.format_products == ["test1, 10000 руб. Остаток: 5 шт.", "test2, 5000 руб. Остаток: 10 шт."]
    assert Category.category_quantity == 1
    assert Category.total_quantity == 2

    product3 = Product("test3", "test description3", 7_000, 15)
    category.add_product(product3)
    assert category.format_products == ["test1, 10000 руб. Остаток: 5 шт.", "test2, 5000 руб. Остаток: 10 шт.", "test3, 7000 руб. Остаток: 15 шт."]
    assert Category.total_quantity == 3

    assert len(category) == 30

    assert str(category) == "test, количество продуктов: 30 шт."

    product4 = Product("test4", "test description4", 8_000, 0)

    with pytest.raises(ValueError):
        category.add_product(product4)

    product5 = Product("test5", "test description5", 9_000, 0)

    products1 = [product4, product5]

    category1 = Category("test1", "test description1", products1)

    assert category1.average_price() == 'Нельзя делить на ноль'


def test_product():
    product = Product("test", "test description", 10_000, 5)
    assert product.name == "test"
    assert product.description == "test description"
    assert product.price == 10_000
    assert product.product_quantity == 5

    product1 = Product.create_product("test1", "test description1", 11_000, 6, )
    assert product1.name == "test1"
    assert product1.description == "test description1"
    assert product1.price == 11_000
    assert product1.product_quantity == 6

    product.price = 12_000
    assert product.price == 12_000

    product2 = Product("test2", "test description2", 13_000, 7)
    assert str(product2) == "test2, 13000 руб. Остаток: 7 шт."

    product3 = Product("test3", "test description3", 14_000, 8)
    assert product + product3 == 172_000


