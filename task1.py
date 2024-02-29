"""
Приложение для выбора пиццы и ее доставки
"""

class Pizza():
    """
    Основной класс, принимающий в себя данные о пицце

    Функция present прредставляет пиццу, ее название, тесто, соус, ингрдиенты (с пиццой барбекю есть возможнсть добавить дополнительный игридиент)

    Также показывается процесс готовки пиццы, на какой стадии готовки.
    """
    def __init__(self, name, dough, sauce, toppings, price):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings
        self.price = price

    def present(self) -> str:
        print(Pizza.name, Pizza.dough, Pizza.sauce, Pizza.toppings)

    def prepare(self) -> str:
        print('Ваша', Pizza.name, 'готовится!')

    def bake(self) -> str:
        print('Ваша', Pizza.name, 'выпекается')

    def cut(self) -> str:
        print('Нарезаем вашу', Pizza.name)

    def box(self) -> str:
        print('Ваша', Pizza.name, 'готова и упакована!')

class PepperonePizza(Pizza):
    """
    Дочерный класс, принимающий в себя данные от Pizza и испольняющий функции родительского класса
    """
    def __init__(self, name, dough, sauce, toppings, price):
        super().__init__(name, dough, sauce, toppings, price)

    def pepperone(self):
        Pizza.present('Пепперони', 'с тонким тестом', 'с томатным соусом', 'с начинкой пепперони, сыр')

    def arrangement(self):
        Pizza.prepare('пепперони')
        Pizza.bake('пепперони')
        Pizza.cut('пепперони')
        Pizza.box('пепперони')

class BBQPizza(Pizza):
    """
    Дочерный класс, с доп функцией выбора доп ингридиента для пиццы
    """
    def __init__(self, name, dough, sauce, toppings, price):
        super().__init__(name, dough, sauce, toppings, price)

    def extratoplings(self, xtratoplings, x, y) -> list:
        self.xtratoplings = ['курица', 'лук', 'сыр']
        self.x = input('Желаете добавить дополнительный ингридиент?')
        self.y = ['Чеснок', 'Яйцо', 'Бекон']
        if x == 'да' or 'Да':
            a = input('Какой ингридиент вы хотите добавить?', y)
            xtratoplings.append(a)
        else:
            pass


    def bbqpizza(self):
        Pizza.present('Барбекью', 'с толстым тестом', 'с соусом барбекью', BBQPizza.extratoplings)

    def arrangement(self):
        Pizza.prepare('пицца барбекью')
        Pizza.bake('пицца барбекью')
        Pizza.cut('пицца барбекью')
        Pizza.box('пицца барбекью')

class SeafoodPizza(Pizza):
    def __init__(self, name, dough, sauce, toppings, price):
        super().__init__(name, dough, sauce, toppings, price)

    def seafood(self):
        Pizza.present('Морская пицца', 'с тонким тестом', 'с горчичным соусом', 'с начинкой осьминог, крабовые палочки, сыр')

    def arrangement(self):
        Pizza.prepare('морская пицца')
        Pizza.bake('морская пицца')
        Pizza.cut('морская пицца')
        Pizza.box('морская пицца')

class Order():
    """
     Class program
    """
    def _init_(self) -> None:
        self.pizzas: list[Pizza] = []

    def add_pizza(self, pizza:Pizza) -> None:
        """ добавляет пиццу"""
        self.pizzas.append(pizza)

    def calculate_total(self) -> int:
        """ возврашает"""
        return sum(pizza.priсe for pizza in self.pizzas)

class Terminal():
    