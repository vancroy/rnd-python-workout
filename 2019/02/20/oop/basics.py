from abc import ABC, abstractmethod


# Класс и создание объекта


class A:
    def __init__(self):
        print('Init A')

    def __del__(self):
        print('destr')


# a = A()

# Статические свойства и методы.

class StaticClass:
    def __init__(self):
        self.a = 'init a'

    a = 'stat'

    @staticmethod
    def static_method():
        print(StaticClass.a)
        # return 'this is static_method'

    @classmethod
    def class_method(cls):
        return cls()

    def method(self):
        return 'method {}'.format(self.a)


# print(StaticClass.static_method())

# sc = StaticClass.static_method()


# StaticClass.a = 'this is static property a'
# print(sc.a)


# print(sc.method())


# Приватные свойства и методы


class PrivateCLass:
    def __init__(self):
        self.publ = 'publ'
        self._priv = 'priv'
        self.__a = 'a'

    def get_a(self):
        return self.__a


pc = PrivateCLass()


# print(pc.publ)
# print(pc._priv)
# print(pc.__prot)

# print(pc.get_a())

# print(pc._PrivateCLass__a)


# Абстрактные методы


class AbstractClass(ABC):
    @abstractmethod
    def some_method(self):
        pass


class C(AbstractClass):
    def __init__(self):
        print('c init')

    # def some_method(self):
    #     pass


c = C()
