'''#Creating a new file
file=open("demo.txt","x")'''

#it has created an empty file


'''#writing into the empty file
file=open("demo.txt","w")
file.write("Hey welcome to the python,This is a new file ")
file.close()

#Reading the created file
file=open("demo.txt","r")
print(file.read())
'''

#deleting a created file
import os
if os.path.exists("demo.txt"):
    print("File exists and it is deleted")
    os.remove("demo.txt")
else:
    print("The file does not exists")

#The file ios deleted