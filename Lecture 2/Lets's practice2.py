#   01

#  WAP to check if a number entered by the user is odd or even.

# num = 14
num = int(input("enter number: "))

rem = num % 2

if(rem == 0):
    print("EVEN")
else:
    print("ODD")









#   02

# WAP to find the greatest of 3 numbers entered by the user


a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
     print("first number is largest", b)
else:
    print("third is largest", c)







#   03

#   WAP to check if a number is a multiple of 7 or not.

x = int(input("enter number: "))

if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")
