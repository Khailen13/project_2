import pytest

from src.category import Category


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
