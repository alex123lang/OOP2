from files.file import products
from category import Category
from product import Product


def main():
    data = products
    for i in data:
        category = Category(i["name"], i["description"], [j["name"] for j in i["products"]])
        print(f'{category.name}\n{category.description}\n{category.products}\n'
              f'Количество категорий: {Category.category_quantity}\n'
              f'Количество продуктов: {Category.total_quantity}\n')

        for j in i["products"]:
            product = Product(j["name"], j["description"], j["price"], j["quantity"])
            print(f'{product.name}\n{product.description}\n{product.price}\n{product.product_quantity}\n')


if __name__ == "__main__":
    main()
