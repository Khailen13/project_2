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
