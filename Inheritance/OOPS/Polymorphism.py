class A:
    def a(self):
        print(".....Welcome.....")
class B(A):
    def a(self):
        print("Good byee.....")
class C(B):
    def a(self):
        print("Get Lost.....")
obj=C()           
obj.a()