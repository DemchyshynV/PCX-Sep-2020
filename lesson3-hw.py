######################################################
# Золушка
######################################################
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'


class Cinderella(Human):
    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size


class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def find_cinderella(self, *cinderellas):
        for cinderella in cinderellas:
            if cinderella.foot_size == self.shoe_size:
                return cinderella


prince = Prince('Max', 16, 36)
print(
    prince.find_cinderella(
        Cinderella('Kira', 16, 25),
        Cinderella('Ira', 20, 35),
        Cinderella('Ilona', 22, 36),
        Cinderella('Marta', 23, 42),
    )
)

"""
 Створити клас rectangle
1) об'єкт приймає два параметри - дві сторони х у
2) описати методи арифметичні
  + сума площин двок об'єктів
  - різниця площин
3) логічні оператори:
  == повертає true якщо рівні по площині
  != якщо не рівні
  >, < відповідно
4) len() - сума сторін
"""

class Rectangle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.__area = x * y

    def __add__(self, other):
        return self.__area + other.__area

    def __sub__(self, other):
        return self.__area - other.__area

    def __eq__(self, other):
        return self.__area == other.__area

    def __ne__(self, other):
        return self.__area != other.__area

    def __gt__(self, other):
        return self.__area > other.__area

    def __lt__(self, other):
        return self.__area < other.__area

    def __len__(self):
        return self.x + self.y


rect1 = Rectangle(2, 5)
rect2 = Rectangle(5, 5)
print(rect1 + rect2)
print(rect1 - rect2)
print(rect1 == rect2)
print(rect1 != rect2)
print(len(rect1))
