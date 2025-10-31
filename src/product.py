from src.base_product import BaseProduct
from src.mixin_info import MixinInfo


class Product(BaseProduct, MixinInfo):
    """Класс для продуктов"""

    name: str
    description: str
    price: float | str
    quantity: int
    general_product_list: list = []

    def __init__(self, name, description, price, quantity) -> None:
        if quantity != 0:
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
            super().__init__()
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

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
