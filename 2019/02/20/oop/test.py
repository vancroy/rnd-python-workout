class Test:
    def __new__(cls, *args, **kwargs):
        print('new')
        obj = super(Test, cls).__new__(cls, *args, **kwargs)

        # print(type(obj))
        print(type(cls))

        return obj

    def __init__(self):
        print('init')

t = Test()




