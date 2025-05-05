class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price

    @classmethod
    def new_product(cls, data: dict):
        return cls(
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            quantity=data.get("quantity"),
        )

    # @classmethod
    # def new_product(cls, name, description, price, quantity):
    #     return cls(name, description, price, quantity)


class Category:
    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1

        Category.product_count += len(products) if products else 0

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str.strip()

    @property
    def products_in_list(self):
        return self.__products
