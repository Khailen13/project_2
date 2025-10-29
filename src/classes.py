class Product:
    """Класс для продуктов"""

    name: str
    description: str
    price: float | str
    quantity: int
    general_product_list: list = []

    def __init__(self, name, description, price, quantity) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.general_product_list.append(
            {
                "name": name,
                "description": description,
                "price": price,
                "quantity": quantity,
            }
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт.\n"

    def __add__(self, other):
        if type(self) is type(other):
            total_price = self.price * self.quantity + other.price * other.quantity
            return total_price
        else:
            raise TypeError

    @classmethod
    def new_product(cls, params: dict):

        try:
            name, description, price, quantity = (
                params["name"],
                params["description"],
                params["price"],
                params["quantity"],
            )
            for product in cls.general_product_list:
                if name == product["name"]:
                    quantity += product["quantity"]
                    price = max(price, product["price"])
            return cls(name, description, price, quantity)
        except Exception:
            pass

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: int | float):
        if new_price > 0:
            if new_price < self.__price:
                price_confirmations = input("Подтверждаете понижение цены? y/n: ")
                if price_confirmations == "y":
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    """Класс для категории продуктов"""

    name: str
    description: str
    products: list | str
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        total_category_products_quantity = 0
        for product in self.__products:
            total_category_products_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_category_products_quantity} шт.\n"

    def add_product(self, product) -> None:
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        result = ""
        for product in self.__products:
            result = result + str(product)
        return result


class CategoryIterator:
    """Класс для перебора товары одной категории"""

    def __init__(self, category_obj):
        self.category = category_obj
        self.products_str_list = self.category.products.split("\n")

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index < len(self.products_str_list) - 2:
            self.index += 1
            return self.products_str_list[self.index]
        else:
            raise StopIteration


class Smartphone(Product):
    """Класс для категории товаров 'Смартфон'"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для категории товаров 'Трава газонная'"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
