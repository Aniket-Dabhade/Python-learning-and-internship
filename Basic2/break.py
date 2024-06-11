#break statement
#Example1
for i in range(10):
    print(i)
    if i==2:
        break
#Example2
s='GeeksforGeeks'
#using a for loop
for letter in s :
    print(letter)
    if letter=='e'or letter=='s':
        break
print("out of the loop")
print()
#using while loop
i=0
while True:
    print(s[i])
    if s[i]=='e' or s[i]=='s':
        break
    i+=1
print(i)
print("out of the while loop")


