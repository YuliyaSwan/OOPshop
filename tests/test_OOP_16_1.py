import pytest

from src.OOP_16_1 import Category, LawnGrass, Product, Smartphone


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


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone3():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category_smartphones(smartphone1, smartphone2):
    return Category("Смартфоны", "Описание", [smartphone1, smartphone2])


@pytest.fixture
def category_grass(grass1, grass2):
    return Category("Газонная трава", "Описание", [grass1, grass2])


def test_product_str(smartphone1):
    assert str(smartphone1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_category_str(category_smartphones):
    assert str(category_smartphones) == "Смартфоны, количество продуктов: 13 шт."


def test_add_product_to_category(category_smartphones, smartphone3):
    category_smartphones.add_product(smartphone3)
    assert smartphone3 in category_smartphones.products_in_list
    assert "Xiaomi Redmi Note 11" in category_smartphones.products


def test_invalid_add_product(category_smartphones):
    with pytest.raises(TypeError):
        category_smartphones.add_product("Not a product")


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


def test_product_addition_1_2(product1, product2):
    total_value = product1.mul + product2.mul
    assert total_value == 2580000.0


def test_product_addition_1_3(product1, product3):
    total_value = product1.mul + product3.mul
    assert total_value == 1334000.0


def test_product_addition_2_3(product2, product3):
    total_value = product2.mul + product3.mul
    assert total_value == 2114000.0


def test_product_addition(smartphone1, smartphone2):
    total = smartphone1 + smartphone2
    assert total == smartphone1.price + smartphone2.price


def test_lawngrass_addition(grass1, grass2):
    total = grass1 + grass2
    assert total == grass1.price + grass2.price


def test_invalid_addition_type(smartphone1, grass1):
    with pytest.raises(TypeError):
        smartphone1 + grass1


def test_add_valid_and_invalid_product(smartphone1, smartphone2, smartphone3, grass1, grass2):
    # Сброс глобального счетчика
    Category.product_count = 0

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    # Добавление корректного продукта
    category_smartphones.add_product(smartphone3)
    assert smartphone3 in category_smartphones.products_in_list

    # Проверка вывода продуктов
    products_output = category_smartphones.products
    assert "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт." in products_output

    products_output_2 = category_grass.products
    assert "Газонная трава, 500.0 руб. Остаток: 20 шт." in products_output_2

    # Проверка количества всех продуктов
    assert Category.product_count == 5  # Всего было создано 5 продуктов


def test_init_smartphone(smartphone1):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_init_grass(grass1):
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


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


def test_category_products_output(category1):
    expected_output = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )
    assert category1.products == expected_output
