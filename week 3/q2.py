# Write a program that simulates the way in which a user might choose a password.
# The program should prompt for a new password, and then prompt again. If the two
# passwords entered are the same the program should say "Password Set" or
# similar, otherwise it should report an error.
import getpass 
# from turtle import goto, label
def getpa():
    password1=getpass.getpass("input password")
    password2=getpass.getpass("confirm password again")
    return password1, password2
p1=""
p2=" "
while p1!=p2:
    print("set new password")
    p1,p2=getpa()
print("password set")