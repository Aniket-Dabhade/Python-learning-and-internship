
#Class And Object
class Detail():
    name ="Rohan"
    age=20
object=Detail()
print("My name is ",object.name)
print("My age is ",object.age)

#Self Parameter

class Details():
    name="Rohan"
    age=20
    def info(self):
        print("My namae is",self.name,"and I'm ",self.age,"Year old")
obj=Details()
obj.info()


#__init()__ function(consturctor)
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=Person("John",20)
print(p.name)
print(p.age)

