from files.file import products
from classes import Category, Product


def main():
    data = products
    for i in data:
        category_count = len(data)
        product_count = len(data[0]["products"]) + len(data[1]["products"])
        category = Category(i["name"], i["description"], [j["name"] for j in i["products"]], category_count, product_count)
        print(f'{category.name}\n{category.description}\n{category.products}\n'
              f'Количество категорий: {category.category_quantity}\n'
              f'Количество продуктов: {category.total_quantity}\n')

        for j in i["products"]:
            product = Product(j["name"], j["description"], j["price"], j["quantity"])
            print(f'{product.name}\n{product.description}\n{product.price}\n{product.product_quantity}\n')


if __name__ == "__main__":
    main()
