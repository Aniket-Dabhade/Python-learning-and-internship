#if statement
if 10>5:
    print("10 is greater than 5")
print("program ended")
#if-else statement
letter ="A"
if letter =="B":
    print("letter is B")
else:
    if letter =="c":
        print("Letter is c")
    else :
        if letter=="A":
            print("Letter is A")
        else :
            print("letter isn't A,B,C ")
#nested if statement

n=10
if n>5:
    print("Bigger than 5")
    if n<=15:
        print("Between 5 and 15")

#if-elif statement
letter="A"
if letter =="B":
    print("Letter is B")
elif letter=="c":
    print("letter is c ")
elif letter=="A":
    print("Letter is A")
else:
    print("Letter isn't A,B,C")