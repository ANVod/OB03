import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Какой-то общий звук")

    def eat(self):
        print(f"{self.name} ест.")

    def to_dict(self):
        return {'type': self.__class__.__name__, 'name': self.name, 'age': self.age}

    @classmethod
    def from_dict(cls, data):
        if data['type'] == 'Bird':
            return Bird(data['name'], data['age'], data['wing_size'])
        elif data['type'] == 'Mammal':
            return Mammal(data['name'], data['age'], data['fur_color'])
        elif data['type'] == 'Reptile':
            return Reptile(data['name'], data['age'], data['scale_texture'])
        else:
            # Возвращает базовое животное, если тип не указан
            return cls(data['name'], data['age'])

# Дополнение методов to_dict() для подклассов
class Bird(Animal):
    def to_dict(self):
        data = super().to_dict()
        data['wing_size'] = self.wing_size
        return data

class Mammal(Animal):
    def to_dict(self):
        data = super().to_dict()
        data['fur_color'] = self.fur_color
        return data

class Reptile(Animal):
    def to_dict(self):
        data = super().to_dict()
        data['scale_texture'] = self.scale_texture
        return data

#
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, person):
        self.staff.append(person)

    def save_to_file(self, filename="zoo_state.json"):
        with open(filename, 'w') as file:
            json.dump([a.to_dict() for a in self.animals], file)

    def load_from_file(self, filename="zoo_state.json"):
        with open(filename) as file:
            animals_data = json.load(file)
            self.animals = [Animal.from_dict(a) for a in animals_data]


# Теперь можно сохранять состояние зоопарка в файл и загружать его
if __name__ == "__main__":
    zoo = Zoo()

    # Здесь можно добавить логику для добавления животных и сотрудников, как ранее

    # После работы
    zoo.save_to_file()

    # Для загрузки состояния
    zoo.load_from_file()