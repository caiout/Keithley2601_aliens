
'''
class A:
    def f(self):
        print('A')

class B:
    def a(self):
        print('B')

class C(A):
    def b(self):
        print('C')

class D(A):
    def c(self):
        print('D')

class E(C,D):
    def d(self):
        print('E')

class F(C,A,D):
    def e(self):
        print('F')

a=F()
print(F.__mro__)
'''


a=23432.771243124
print(round(a,2))