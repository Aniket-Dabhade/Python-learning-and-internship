'''#try And Except Block

try:
    num = int(input("Enetr an Integer : "))
except ValueError:
    print("Number entered is not  an integer")


#finally keyword

try :
    num=int(input("Enetr an Integer : "))
except ValueError:
    print("Number entered is not an integer")
else :
    print("Integer Accepted")
finally:
    print("This block is always executed")

#raise keyword


salary=int(input("Enter your salary : "))
if not 2000<salary<5000:
    raise ValueError("Not a valide salary")
'''
#example of try and except
print("Start")
n1=int(input("Enter first number : "))
n2=int(input("Enter second number : "))
try:
    print(n1/n2)
except:
    print("Number can not be devided by 0")