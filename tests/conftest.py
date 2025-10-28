import pytest

from src.classes import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def product1():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    return product


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def product4():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def category1():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [],
    )


@pytest.fixture
def category2():
    return Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [],
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
