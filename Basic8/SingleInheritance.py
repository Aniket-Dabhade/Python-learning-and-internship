#Single Inheritance

class Parent:
    def fun1(self):
        print("This function is in parent class")
class Child(Parent):
    def fun2(self):
        print("This function is is child class")
obj=Child()
obj.fun1()
obj.fun2()