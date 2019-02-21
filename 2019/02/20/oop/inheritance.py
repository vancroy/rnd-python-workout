# Наследование от int


class A(int):
    def __new__(cls, value, *args, **kwargs):
        return super(A, cls).__new__(cls, value)

    def inc(self):
        return self + 1


# i = 5
# j = A(10)
# k = i + j

# print(i, j, k)

# l = i.inc()
# m = j.inc()
#
# print(l)
# print(m)


# Ромбовидное наследование, Порядок разрешения методов (MRO)


class A:
    def m(self):
        print("m of A called")


class B(A):
    pass
    # def m(self):
    #     print("m of B called")


class C(B):
    pass
    # def m(self):
    #     print("m of C called")


class D(B, C, A):
    pass


x = D()
x.m()
