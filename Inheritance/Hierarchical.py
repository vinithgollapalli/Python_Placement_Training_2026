class Parent1:
    def land(self):
        print("I have 10 acers of Land")
class Son(Parent1):
    pass
class Daughter(Parent1):
    pass
obj=Son()
obj.land()
obj=Daughter()
obj.land()
