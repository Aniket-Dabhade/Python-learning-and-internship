'''#Global and Local variable
x=10 #global variable
def myfun():
    y=5 #local variable
    print(y)
myfun()
print(x)
print(y) #it will generate an eerror as it is a local variable
'''
#Global keyword

x=10 #global variable
def myfun():
    global x
    x=5
    y=5 #local variable
    print(y)
myfun()
print(x)
print(y) #it will generate an eerror as it is a local variable