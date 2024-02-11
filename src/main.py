from files.file import products
from category import Category
from product import Product


def main():
    data = products
    categories = []
    for i in data:
        products_in_category = []

        for j in i["products"]:
            product = Product(j["name"], j["description"], j["price"], j["quantity"])
            products_in_category.append(product)

        category = Category(i["name"], i["description"], products_in_category)
        categories.append(category)

    for category in categories:
        print(f'{category.name}\n{category.description}\n{category.format_products}\n')

        for product in category.products:
            print(f'{product.name}\n{product.description}\n{product.price}\n{product.product_quantity}\n')

    print(f'Количество категорий: {Category.category_quantity}\n'
          f'Количество продуктов: {Category.total_quantity}\n')


if __name__ == "__main__":
    main()
