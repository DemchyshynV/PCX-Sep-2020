# s = {1, 2, 3, 4, 4, 5, 6, 1}
# s = {}
# s = set()
# s.add(1)
# s.add(1)
# s.add(2)
# l = [1,2,3,4,1,2,4,2]
# s1 = set(l)
# print(s1)
s1 = {10, 13, 27, 1}
s2 = {5, 1, 6, 2}

# print(s1.issuperset(s2))
# print(s2.issubset(s1))
# print(s1.isdisjoint(s2))
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))


# # s1.remove(22)
# s1.discard(22)
# pop = s1.pop()
# print(pop)
# print(s1)

###############################################################
# string
###############################################################

# string = "name = \"Vasia\""
# print(string)

# string = '*' * 10
# # print(string)
# name = 'Max'
# age = 18
# weight = 70.5
# string = 'Hello, my name is Max, I`m 18 and my weight 70.5 kg'
# string = 'Hello, my name is ' + name + ', I`m ' + str(age) + ' and my weight ' + str(weight) + ' kg'
# string = 'Hello, my name is %s, I`m %d and my weight %f kg' % (name, age, weight)
# string = 'Hello, my name is {}, I`m {} and my weight {} kg'.format (name, age, weight)
# string = 'Hello, my name is {name}, I`m {age} and my weight {weight} kg'.format(age=age, weight=weight, name=name)
# string = f'Hello, my name is {name}, I`m {age} and my weight {weight} kg'
# print(string)
#
# # print(string[:5])
# string = '    aaaaa        '
# strip = string.rstrip()
# print([strip])


# string = 'Hello from OWU'
# # partition= string.partition('from')
# # print(partition)
# replace = string.replace('o', 'll')
# print(replace)

# min_num = min([1, 2, 3, -12, 4])
# min_num = max([1, 2, 3, -12, 4])
# min_num = sorted([1, 2, 3, -12, 4], reverse=True)
# f = pow(2, 255)
# print(f)

# l2 = [i for i in range(10)]
# print(l2)
# l3 = [i + 1 for i in l2 if i % 2 == 0]
# l3 = [i + 1 if i % 2 == 0 else i for i in l2]
# print(l3)
# l1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#
# res = [i for item in l1 for i in item]
# print(res)

# def func(a=5,b=5,c=5, *args):
#     print(a,b,c, args)
#
# func(5,5,5,6,7,8, name='Max', age=14)

#

#
#
# def decor(func, *args, **kwargs):
#     print('-----------------------------------')
#     func(*args, **kwargs)
#     print('-----------------------------------')
#
#
# decor(greeting, 'OWU')
#

# def decor(func):
#     def wrap(*args, **kwargs):
#         print('-------------------------------')
#         func(*args, **kwargs)
#         print('-------------------------------')
#
#     return wrap
#
#
# @decor
# def greeting(str):
#     print(f'Hello {str}')
# @decor
# def summator(a,b):
#     print(a+b)
#
# greeting('Max')
# summator(2,5)
# l = [1, 2, 3, 4, 6]
# def inc(x):
#     return x+1

# #
# map_list = map(lambda x: x*2, l)
# print(list(map_list))
#
# # const func = (x)=>x+1
# # func = lambda x:x+1

# def clousures():
#     count = 0
#     def wrap():

# a = 5
# b = 6
# b,a = [a,b]
#
# c = (b, a)

# print(type(c))
# print(a,b)

# l = [1, 2, 3, 4, 5, 6]
#
# a, _, b,*_, c,d = l
# print(a, b, c,d)


d = {
    'arg1': 15,
    'arg2': 15,
    'arg3': 15,

}
get = d.get('arg2')
print(get)


def func(arg1, arg2, arg3):
    return arg1 + arg2 + arg3


print(func(**d))
