# def func(arr: str) -> str:
#     return ''

# for i in range(10):
#     a=10
# a = 'global'
# def aa():
#     # a = 'a'
#     def b():
#         # a = 'b'
#         def c():
#             # nonlocal a
#             global a
#             a = 'c'
#             print(a)
#         c()
#         print(a)
#     b()
#     print(a)
# aa()
# print(a)

# def counter():
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         print(count)
#
#     return wrap
#
#
# c1 = counter()
# c2 = counter()
#
# c1()
# c1()
# c1()
# c1()
# c2()
# c1()
# c2()
################################
# CLASSES
################################
#
# class First:
#     __count = 0
#
#
# print(First._First__count)
# # First.

# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def __set_name(self, name):
#         self.__name = name
#
#     def __get_name(self):
#         return self.__name
#
#     def __del_name(self):
#         del self.__name
#     my_name = property(fset=__set_name, fget=__get_name, fdel=__del_name)
#
#
# user = User('Max')
# user.my_name = 5
# print(user.my_name)
# del user.my_name
#
# #
# # user = User('Max')
# #
# # print(user.name)
# # user.name = 'Karina'
# # print(user.name)
# # print(user.__dict__)
# # del user.name
# # print(user.name)
# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name


# user = User('Max')
# # user.name
# user.name = 'Karina'
# print(user.name)
# del user.name
# print(user.name)

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#     def info(self):
#         return 'This is a car'
#
#
# class Radio:
#     def play_music(self):
#         print('lalalala')
#
#
# class DiselCar(Car):
#     def __init__(self, brand, model, tnvd):
#         super().__init__(brand, model)
#         self.tnvd = tnvd
#
#     def info(self):
#         return f'{super().info()} Disel'
#
#
# bmw = DiselCar('BMW', 's3', True)
# print(bmw.info())
#
#
# class PetrolCar(Car, Radio):
#     def __init__(self, brand, model, num):
#         super().__init__(brand, model)
#         self.num = num
#
#     def info(self):
#         print(self.num)
#
#
# kia = PetrolCar('KIA', 'ex', 95)
#
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def perimeter(self):
#         return self.a + self.b
#
#     def area(self):
#         return self.a * self.b
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         return self.a * self.b / self.c
#
#     def area(self):
#         return self.a * self.b + self.c
#
#
# shapes = [Triangle(3, 4, 5), Triangle(4, 5, 6), Rectangle(2, 3)]
#
#
# for shape in shapes:
#     print(shape.perimeter())
#     print(shape.area())

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} - {self.age}'

    def __repr__(self):
        return f'{self.name} - {self.age}'

    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        return self.age + other.age

    def __sub__(self, other):
        return self.age - other.age
    def __mul__(self, other):
        return self.age * other.age


user1 = User('Maryana', 25)
user2 = User('Maryana', 24)
user3 = User('Maryana', 23)
users = [user1, user2, user3]
print(len(user1))

print(users)
print(user1 - user2)
