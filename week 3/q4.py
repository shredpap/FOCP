# Modify your program again so that the chosen password cannot be one of a list of
# common passwords, defined thus:
# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
import getpass 
def getpa():
    password1=getpass.getpass("input password")
    password2=getpass.getpass("confirm password again")
    return password1, password2
p1=""
p2=""
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:
    print("set new password")
    p1,p2=getpa()
    if p1==p2 and 12>=len(p1)>=8 and not (p1 in BAD_PASSWORDS):
        print("okay")
        break
print("password set")
