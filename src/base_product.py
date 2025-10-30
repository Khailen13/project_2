from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс с именем BaseProduct, который является родительским для классов продуктов"""

    @abstractmethod
    def __init__(self):
        super().__init__()

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, params: dict):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price):
        pass
