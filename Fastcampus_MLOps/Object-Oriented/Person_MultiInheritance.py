class A:
    def method(self):
        print("Class A's method")
        
class B(A):
    def method(self):
        print("Class B's method")
        
class C(A):
    def method(self):
        print("Class C's method")

class D(B, C):
    pass

d = D()
d.method()
print(D.mro()) # 다중상속 호출 우선순위 확인 가능