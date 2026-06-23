class Parent1:
    def land(self):
        print("I have 10 acers of Land")
class Parent2(Parent1):
    def gold(self):
        print("I have 100 grams of gold")
class Child(Parent2):
    pass
class Child2(Parent2):
    pass
obj=Child()
obj.land()
obj.gold()
obj=Child2()
obj.land()
obj.gold()