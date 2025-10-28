import pytest

from src.classes import Category, CategoryIterator, LawnGrass, Product, Smartphone


def test_product_init(product1, product2, product3, product4):
    """Проверка корректности инициализации объектов класса Product"""

    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 210000.0
    assert product2.quantity == 8

    assert product3.name == "Xiaomi Redmi Note 11"
    assert product3.description == "1024GB, Синий"
    assert product3.price == 31000.0
    assert product3.quantity == 14

    assert product4.name == '55" QLED 4K'
    assert product4.description == "Фоновая подсветка"
    assert product4.price == 123000.0
    assert product4.quantity == 7


def test_product_new_product():
    """Проверка атрибута new_product при добавлении новых продуктов:
    с разными именами, с идентичным именем и с ошибочным ключом"""

    # Добавление продукта "Продукт_A"
    product_a_parameters = {
        "name": "Продукт_A",
        "description": "Описание продукта_A",
        "price": 100,
        "quantity": 5,
    }
    product_a = Product.new_product(product_a_parameters)
    assert product_a.name == product_a_parameters["name"]
    assert product_a.description == product_a_parameters["description"]
    assert product_a.price == product_a_parameters["price"]
    assert product_a.quantity == product_a_parameters["quantity"]

    # Добавление продукта "Продукт_B"
    product_b_parameters = {
        "name": "Продукт_B",
        "description": "Описание продукта_B",
        "price": 100,
        "quantity": 1,
    }
    product_b = Product.new_product(product_b_parameters)
    assert product_b.name == product_b_parameters["name"]
    assert product_b.description == product_b_parameters["description"]
    assert product_b.price == product_b_parameters["price"]
    assert product_b.quantity == product_b_parameters["quantity"]

    # Добавление продукта "Продукт_A" с большей стоимостью
    product_c_parameters = {
        "name": "Продукт_A",
        "description": "Описание продукта_A",
        "price": 120,
        "quantity": 10,
    }
    product_c = Product.new_product(product_c_parameters)
    assert product_c.quantity == product_a_parameters["quantity"] + product_c_parameters["quantity"]
    assert product_c.price == max(product_a_parameters["price"], product_c_parameters["price"])

    # Добавление продукта "Продукт_Д" с ошибочным ключом
    product_d_parameters = {
        "Ключ вместо name": "Продукт_Д",
        "description": "Описание продукта_Д",
        "price": 100,
        "quantity": 5,
    }
    with pytest.raises(AttributeError):
        product_d = Product.new_product(product_d_parameters)
        product_d.name


def test_product_price_setter(capsys):
    """Проверка сеттера price"""

    # Создание нового экземпляра
    product_e_parameters = {
        "name": "Продукт_Д",
        "description": "Описание продукта_Д",
        "price": 1000,
        "quantity": 10,
    }
    product_e = Product.new_product(product_e_parameters)
    assert product_e.price == 1000

    # Изменение цены на большее
    product_e.price = 1200
    assert product_e.price == 1200

    # Попытка назначения цене отрицательное значения
    product_e.price = -100
    message = capsys.readouterr()
    assert message.out == "Цена не должна быть нулевая или отрицательная\n"


def test_product_str(product1, product2, product3):
    """Проверка строкового отображения"""

    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    assert str(product2) == "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    assert str(product3) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"


def test_product_add(product1, product2, product3, smartphone1, grass1):
    """Проверка сложения продуктов"""

    assert product1 + product2 == 2580000.0
    assert product1 + product3 == 1334000.0
    assert product2 + product3 == 2114000.0
    with pytest.raises(TypeError):
        smartphone1 + grass1


def test_category_init_add_product_count(category1, category2, product1, product2, product4, smartphone1, smartphone2):
    """Проверка корректности инициализации, добавления продуктов,
    подсчета количества продуктов и категорий объектов класса Category"""

    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert Category.category_count == 2
    assert Category.product_count == 0
    assert category1.products == ""
    assert Category.product_count == 0
    category1.add_product(product1)
    assert category1.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    assert Category.product_count == 1
    assert category2.name == "Телевизоры"
    assert (
        category2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category2.products == ""
    category2.add_product(product4)
    assert category2.products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
    assert Category.product_count == 2
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1])
    with pytest.raises(TypeError):
        category_smartphones.add_product("Not a product")


def test_category_str(category1, product1, product2):
    """Проверка строкового отображения"""

    assert str(category1) == "Смартфоны, количество продуктов: 0 шт.\n"
    category1.add_product(product1)
    assert str(category1) == "Смартфоны, количество продуктов: 5 шт.\n"
    category1.add_product(product2)
    assert str(category1) == "Смартфоны, количество продуктов: 13 шт.\n"


def test_category_iterator(category1, product1, product2):
    """Проверка итератора категорий"""

    category1.add_product(product1)
    category1.add_product(product2)
    products_list = []
    for i in CategoryIterator(category1):
        products_list.append(i)

    assert len(products_list) == 2
    assert products_list[0] == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert products_list[1] == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_smartphone_init(smartphone1):
    """Проверка инициализации"""

    assert type(smartphone1) is Smartphone
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_lawngrass_init(grass1):
    """Проверка инициализации"""

    assert type(grass1) is LawnGrass
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"
