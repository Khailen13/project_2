class Product:
    """Класс для продуктов"""

    name: str
    description: str
    price: float | str
    quantity: int
    general_product_list: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
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

    def add_product(self, product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result
