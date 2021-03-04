class User:
    __count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.__count += 1

    def info(self):
        print(self.__dict__)

    @staticmethod
    def greeting():
        print('Hello world')

    @classmethod
    def get_count(cls):
        print(cls.__count)

    @classmethod
    def create_user(cls, name, age):
        return cls(name, age)


user = User('Max', 2)
user.info()
user.greeting()
User.greeting()
User.get_count()
# user.get_count()
kira = User.create_user('Kira', 25)
kira.info()
