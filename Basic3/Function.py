#function with non parametrer
def fun():
    print("Welcome to python")

fun()

#function with parameter
def is_prime(n):
    if n in[2,3]:
        return True
    if(n==1)or(n%2==0):
        return False
    r=3
    while r*r<=n:
        if n%r==0:
            return False
        r+=2
        return True

a=int(input("enter a number : "))
print(" The number is ",is_prime(a))

#Argument of python funtion
def evenodd(x):
    if x%2==0 :
        print("even")
    else :
        print("Odd")
evenodd(7)

#Default argument
def MyFun(x,y=30):
    print("x :",x)
    print("y :",y)
MyFun(10)


#Keyword argument
def Student(firstname,lastname):
    print(firstname,lastname)
Student(firstname='Aniket',lastname='Dabhade')
Student('Aniket','Dabhade')
Student(lastname='Dabhade',firstname='Aniket')

#variable length argument
def myfun(*argv):
    for arg in argv:
        print(arg)
myfun('Hello','welcome','to','python')

#doctstring
def evenOdd(x):
    '''function to check whether the x is even or odd)'''
    if x%2==0:
        print("even")
    else:
        print("odd")
print(evenOdd.__doc__)

#Return ststement in python
def square_value(num):
    return num **2
print("Square is ",square_value(2))

#pass by reference or value

def myFun(x):
    x[0]=20
lst=[10,11,12,13,14,15]
myFun(lst)
print(lst)
