from src.product import Product


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
