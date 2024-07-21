#Hierarchical inheritance

class Parent:
    def fun1(self):
        print("This function is in parent class")

class Child1(Parent):
    def fun2(self):
        print("This function is in Child1 class")

class Child2(Parent):
    def fun3(self):
        print("This function is in Child2 class")

obj1=Child1()
obj2=Child2()
obj1.fun1()
obj1.fun2()
obj2.fun1()
obj2.fun3()
