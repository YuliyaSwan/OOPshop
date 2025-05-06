import json
import os

from src.OOP_16_1 import Category, Product


def load_products(file_path: str):
    """
    Загружает данные из JSON-файла.
    """
    if not os.path.exists(file_path):
        print("Файл не найден.")
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            print("Ошибка при чтении JSON.")
            return []


def create_objects_from_json(data):
    """
    Создает объекты категорий и продуктов.
    """
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(name=category["name"], description=category["description"], products=products))
    return categories


if __name__ == "__main__":
    data = load_products("../data/products.json")
    categories = create_objects_from_json(data)

    for category in categories:
        print(category.name)
        print(category.description)
        for product in category.products:
            print(f"  - {product}")
