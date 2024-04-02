# Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и
# переопределите методы, если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать
# информацию о животных и сотрудниках. Должны быть методы для добавления животных и
# сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()`
# для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
# Базовый класс Animal
# Базовый класс Животное
# Базовый класс Животное
import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Какой-то общий звук")

    def eat(self):
        print(f"{self.name} ест.")


# Подклассы Animal
class Bird(Animal):
    def __init__(self, name, age, wing_size):
        super().__init__(name, age)
        self.wing_size = wing_size

    def make_sound(self):
        print(f"{self.name} чирикает.")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} издает звук млекопитающего.")


class Reptile(Animal):
    def __init__(self, name, age, scale_texture):
        super().__init__(name, age)
        self.scale_texture = scale_texture

    def make_sound(self):
        print(f"{self.name} шипит.")


# Полиморфизм
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# Класс зоопарка с композицией
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, person):
        self.staff.append(person)


# Классы сотрудников
class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")


# Тестирование
if __name__ == "__main__":
    zoo = Zoo()

    # Создание животных
    tweety = Bird("Чиж", 2, "маленький")
    tom = Mammal("Барсик", 5, "серый")
    sammy = Reptile("Каа", 3, "шершавый")

    # Добавление животных в зоопарк
    zoo.add_animal(tweety)
    zoo.add_animal(tom)
    zoo.add_animal(sammy)

    # Создание и добавление сотрудников
    bob = ZooKeeper("Василий")
    alice = Veterinarian("Елена")

    zoo.add_staff(bob)
    zoo.add_staff(alice)

    # Демонстрация полиморфизма
    animal_sound(zoo.animals)

    # Сотрудники работают с животными
    bob.feed_animal(tom)
    alice.heal_animal(sammy)
if __name__ == "__main__":
    zoo = Zoo()

    # Создание животных
    tweety = Bird("Твити", 2, "маленький")
    tom = Mammal("Том", 5, "серый")
    sammy = Reptile("Сэмми", 3, "шершавый")

    # Добавление животных в зоопарк
    zoo.add_animal(tweety)
    zoo.add_animal(tom)
    zoo.add_animal(sammy)

    # Создание и добавление сотрудников
    bob = ZooKeeper("Боб")
    alice = Veterinarian("Алиса")

    zoo.add_staff(bob)
    zoo.add_staff(alice)

    # Демонстрация полиморфизма
    animal_sound(zoo.animals)

    # Сотрудники работают с животными
    bob.feed_animal(tom)
    alice.heal_animal(sammy)