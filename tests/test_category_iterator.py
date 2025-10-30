from src.category_iterator import CategoryIterator


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
