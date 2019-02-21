# Топорный способ


class A:
    def __init__(self):
        self._x = ''

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value.strip(' \t\r\n')


# a = A()
# a.set_x('test    ')
# print('>{}<'.format(a.get_x()))

# Более правильный способ - через декораторы


class B:
    def __init__(self):
        self._x = 'init x'

    @property
    def x(self):
        return self._x
    #
    # @x.setter
    # def x(self, value):
    #     self._x = value


b = B()
# b.x = 'test'
print(b.x)
