from src.lawn_grass import LawnGrass


def test_lawn_grass_init(grass1):
    """Проверка инициализации"""

    assert type(grass1) is LawnGrass
    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"
