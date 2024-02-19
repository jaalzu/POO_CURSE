class A:
    def hablar(self):
        print("Hola desde A")
class B(A):
    def hablar(self):
        print("Hola desde B")
class C(A):
    def hablar(self):
        print("Hola desde C")
class D(B,C):
    def hablar(self):
        print("hola desde D")

d = D()

d.hablar()




# class X:pass
# class Y:pass
# class Z:pass
# class A(X,Y):pass
# class B(Y,Z):pass
# class M(B,A,Z):pass



# print(M.mro())



# O = object
# class F(O): pass
# class E(O): pass
# class D(O): pass
# class C(D,F): pass
# class B(E,D): pass
# class A(B,C): pass

# print(A.mro())