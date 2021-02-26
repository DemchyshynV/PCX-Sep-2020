# for i in range(20):
#     a = 10
#
# print(i)
# print(a)
# if True:
#     b = 20
#     print(globals())
#
#
# print(locals().get('b'))
# name = 'Max'
# print(locals())
#
# def a():
#     name = 'a'
#
#     def b():
#         # name = 'b'
#
#         def c():
#             nonlocal name
#             name = 5
#         c()
#
#     b()
#     print(name)
#
#
# a()
######################################################
# COUNTER
########################################################
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
# c2()
# c2()
# c2()
# c1()

########################################################
# CLASES
########################################################

# public protected private

# class First(object):
#     _count = 0


# f = First()
# f2 = First()
# print(f.__dict__)
# print(First.__dict__)
# print(First.count)

# class Second(First):
#     pass
#
#
# print(Second._count)
#########################################################################################
# Инкапсуляция
#########################################################################################
# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def delete_name(self):
#         del self.__name
#
#
# user = User('Max')
# print(user.get_name())
# user.set_name('Vasia')
# print(user.get_name())
# user.delete_name()
# print(user.__dict__)


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
#     def __delete_name(self):
#         del self.__name
#     my_name = property(fset=__set_name, fget=__get_name, fdel=__delete_name)
#
#
# user = User('Max')
# user.my_name = 5
# print(user.my_name)
# del user.my_name
# print(user.__dict__)


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
#
#
# user = User('Max')
# print(user.name)
# user.name = 'Vasia'
# del user.name
# print(user.__dict__)
# Many Extends

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return 'This is a car'


class DiselCar(Car):
    def __init__(self, brand, model, tnvd):
        super().__init__(brand, model)
        self.tnvd = tnvd

    def info(self):
        print(f'{super().info()} and Disel')


class PetrolCar(Car):
    def __init__(self, brand, model, octan_number):
        super().__init__(brand, model)
        self.octan_number = octan_number


car = DiselCar('BMW', 's3', True)
car.info()

