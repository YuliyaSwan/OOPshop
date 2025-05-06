import pytest

from src.OOP_15_1 import Category, Product


@pytest.fixture
def product1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def category1(product1, product2, product3):
    Category.category_count = 0
    Category.product_count = 0
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


# @pytest.fixture
# def category1():
#     return Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [
#             {
#                 "name": "Samsung Galaxy C23 Ultra",
#                 "description": "256GB, Серый цвет, 200MP камера",
#                 "price": 180000.0,
#                 "quantity": 5,
#             },
#             {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
#             {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
#         ],
#     )


def test_init(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5
    assert product1.mul == 900000.0


def test_product_price_setter(product1):
    product1.price = 800
    assert product1.price == 800


def test_product_price_setter_error(product1, capfd):
    original_price = product1.price
    product1.price = 0
    out, _ = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert product1.price == original_price

    product1.price = -100
    out, _ = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert product1.price == original_price


def test_product_new_product():
    data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_str(product1):
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_addition_1_2(product1, product2):
    total_value = product1.mul + product2.mul
    assert total_value == 2580000.0


def test_product_addition_1_3(product1, product3):
    total_value = product1.mul + product3.mul
    assert total_value == 1334000.0


def test_product_addition_2_3(product2, product3):
    total_value = product2.mul + product3.mul
    assert total_value == 2114000.0


def test_init_cat(category1):
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    expected_output = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )
    assert category1.products == expected_output
    # assert category1.products_in_list == [
    #     {
    #         "name": "Samsung Galaxy C23 Ultra",
    #         "description": "256GB, Серый цвет, 200MP камера",
    #         "price": 180000.0,
    #         "quantity": 5,
    #     },
    #     {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
    #     {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
    # ]
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_category_add_product(category1):
    new_product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(new_product)
    assert '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.' in category1.products
    assert Category.product_count == 4


def test_category_products_in_list(category1):
    result = category1.products_in_list
    assert isinstance(result, list)
    assert all(isinstance(product, Product) for product in result)


def test_category_str(category1):
    # Общий остаток: 5 + 8 + 14 = 27
    assert str(category1) == "Смартфоны, количество продуктов: 27 шт."


def test_category_products_output(category1):
    expected_output = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )
    assert category1.products == expected_output
