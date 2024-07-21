class School:
    def fun1(self):
        print("This function is in School")


class Student1(School):
    def fun2(self):
        print("This function is in Student 1")


class Student2(School):
    def fun3(self):
        print("This function is in Student 2")

class Student3(Student1,School):
    def fun4(self):
        print("This function is in Student 3")

obj=Student3()
obj.fun1()
obj.fun2()