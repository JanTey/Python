# Наследование
class Human():
    name = ''
    gender = ''
    height = 0
    weight = 0
    hands = 2
class Spider():
    gender = ''
    height = 0
    weight = 0
    hands = 6

    def webshoot(self):
        print('Pew-Pew!')

# class SpiderMan(Human, Spider): здесь будет у SpiderMan 2 руки
class SpiderMan(Spider, Human): # а здесь будет 6 рук, т.к. наследование первое стоит Spider
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

peter_parker = SpiderMan('Peter Parker', 'Male')
print(peter_parker.name)
print(peter_parker.gender)
print(peter_parker.height)
print(peter_parker.weight)
print(peter_parker.hands)
peter_parker.webshoot()
print()
print(SpiderMan.mro())

# функция super() позволяет напрямую использовать атрибуты родительского класса
print()
class Human():
    def __init__(self, name, gender, height=0, weight=0, hands=2):
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.hands = hands

class Spider():
    def __init__(self, gender, height=0, weight=0, hands=6):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.hands = hands

    def webshoot(self):
        print('Pew-Pew!')

class SpiderMan(Human, Spider):
    def __init__(self, name, gender):
        self.weapons = []
        # Вызываем конструктор родительского класса, чтобы взять и инициализировать нужные атрибуты оттуда
        super().__init__(name, gender)
    def attack(self):
        if 'web' in self.weapons:
            super().webshoot()
        else:
            print('No web!')
peter_parker = SpiderMan('Peter Parker', 'Male')
peter_parker.attack()

peter_parker.weapons.append('web')
peter_parker.attack()
print()
print(SpiderMan.mro())
print()

# Полиморфизм - свойство системы использовать объекты с одинаковым интерфейсом без информации о типе
# и внутренней структуре объекта

class Human():
    def __init__(self, name, gender, height=0, weight=0, hands=2):
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.hands = hands
    def move(self):
        self.weight -= 0.01

class Spider():
    def __init__(self, gender, height=0, weight=0, hands=6):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.hands = hands

    def webshoot(self):
        print('Pew-Pew!')

class SpiderMan(Human, Spider):
    def __init__(self, name, gender):
        self.weapons = []
        super().__init__(name, gender)
    def attack(self):
        if 'web' in self.weapons:
            super().webshoot()
        else:
            print('No web!')
# мы можем переопределить метод родительского класса на какой-то другой функционал
    def move(self):
        super().webshoot()
        super().move()

peter_parker = SpiderMan('Peter Parker', 'Male')
print(peter_parker.weight)
peter_parker.move()
print(peter_parker.weight)
print()

# магические методы

class Human():
    def __init__(self, name, gender, height=0, weight=0, hands=2):
        self.name = name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.hands = hands
    def move(self):
        self.weight -= 0.01

class Spider():
    def __init__(self, gender, height=0, weight=0, hands=6):
        self.gender = gender
        self.height = height
        self.weight = weight
        self.hands = hands

    def webshoot(self):
        print('Pew-Pew!')

class SpiderMan(Human, Spider):
    def __init__(self, name, gender):
        self.weapons = []
        super().__init__(name, gender)
    def attack(self):
        if 'web' in self.weapons:
            super().webshoot()
        else:
            print('No web!')
    def move(self):
        super().webshoot()
        super().move()
# Добавим возможность сравнения персонажей
    def __lt__(self, other):
        if not isinstance(other, SpiderMan):
            print('Not SpiderMan!')
        return len(self.weapons) < len(other.weapons)

    def __add__(self, weapon):
        if not isinstance(weapon, str):
            print('Error')
            return
        self.weapons.append(weapon)

peter_parker = SpiderMan('Peter Parker', 'Male')
miles_morales = SpiderMan('Miles Morales', 'Male')
peter_parker.weapons += ['web_shooter']
print(peter_parker.weapons)
# miles_morales.weapons += ['web_shooter', 'electricity']
# print(miles_morales.weapons)
# print(peter_parker < miles_morales)
# print(peter_parker > miles_morales)

# peter_parker.weapons
peter_parker + 'strike'
# peter_parker.weapons
print(peter_parker.weapons)