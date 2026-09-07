age = 21

if age >= 18:
    print("Can vote")
    print("Can drive")





#   02

light = "green"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")


print("end of code")



#   03

num = 5

if(num > 2):
    print("greater than 2")
if(num > 3):
    print("greater than 3")

print("end of code")



#   04

# age = 24
age = 24

if(age >= 18):
    print("can vote")  # indentation error  {}
else:
    print("CANNOT vote")







#   05

# marks = 74
marks = int(input("enter student marks: "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"

print("grade of the student ->", grade)
