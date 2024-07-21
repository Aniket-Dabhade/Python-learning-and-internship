#Multilevel Inheritance

class Grandfather:
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername


class Father(Grandfather):
    def __init__(self,fathername,grandfathername):
        self.fathername=fathername
        Grandfather.__init__(self,grandfathername)


class Son(Father):
    def __init__(self,sonname,fathername,grandfathername):
        self.sonname=sonname
        Father.__init__(self,fathername,grandfathername)


    def print_name(self):
        print("Grandfather name is :",self.grandfathername)
        print("father name is :", self.fathername)
        print("Son name is :", self.sonname)


s1=Son("Aniket","Keshav","Amrut")
print(s1.grandfathername)
s1.print_name()