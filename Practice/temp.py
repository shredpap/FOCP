# total = 98.2
# count=5

# #add your extra code here
# avg=total/count
# print("The average is", avg)

#######################

# name=input("What's your name? \n")
# age=int(input("Enter your age? \n"))
# print(f"Hello There, {name} \n Your age is: \n Your name length is: {len(name)}")

#######################

# age=input("Enter your age ")
# age=int(age)
# print(f"in one year your age will be {age+1}")

#######################

# a,b=int(input("Enter first number: ")), int(input("Enter second number: "))
# print(a*b)

#######################

# comment="I would have"thought" you knew better!"
# print(comment)

#######################

# print("This test includes characters such as '\' '"' and "'",\n\tThis is a new line starts with a tab\n\t\tThis new line starts with two tabs")

#######################

# print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\nHello there!\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

#######################

# print("""This text spans three lines,
# and includes both single('),
# and double quotes(").""")

#######################

# surname="Palin"
# val=surname[:-1]
# print(val)

#######################

# primes=[2,3,5,7,13,17,19,23,29,31,37,41,43,47]
# sliced=primes[:4]
# print(sliced)

#######################

# names=['Barry', 'Michelle', 'Marin']
# name1,name2=input("Enter first name to add in list: "),input("Enter second name to add in list: ")
# names.insert(-1,name1)
# names.insert(-1,name2)
# print(names)

#######################

# import math
# print(math.sqrt(2401))

#######################

# from math import log2
# print(log2(1024))

#######################

# def displayTwice(msg):
#     """Fuction to print the message passed on the parameters"""
#     print(msg)
#     print(msg)
# displayTwice("One")
# displayTwice("Piece")
# help(displayTwice)

#######################

# def findMax(a,b):
#     """Finds the maximum of two values."""
#     if ( a > b ):
#         max = a
#     else:
#         max = b
#     return max
# findMax(1,2)
# findMax(15,99)
# findMax(10,15)

######################

# def multi(val1,val2=0):
#     if val2==0:
#         return val1**2
#     else:
#         return val1*val2
# print(multi(4,1))

######################

# def someFunc(x, y, z):
# 	print("x is", x, "\ny is", y, "\nz is", z)
# someFunc(y=10,x=3,z=33)
# someFunc(z=33,y=55,x=90)
# someFunc(12,13,14)

######################

# print("hello","!","jjj",sep="world")

######################

# def calcAve(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total/len(numbers)
# print(calcAve(1,2,3))
# print(calcAve(4,5,6))
# print(calcAve(10,20,30))
# print(calcAve(30,15,0))

######################

# to_seconds=lambda a,b=0 : (a*3600)+(b*60)
# print(to_seconds(1))
# print(to_seconds(2))

######################