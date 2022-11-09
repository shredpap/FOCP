# Modify your program a final time so that it executes until the user successfully
# chooses a password. That is, if the password chosen fails any of the checks, the
# program should return to asking for the password the first time.

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
