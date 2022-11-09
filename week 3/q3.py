# Modify your previous program so that the password must be between 8 and 12
# characters (inclusive) long.
import getpass 
def getpa():
    password1=getpass.getpass("input password")
    password2=getpass.getpass("confirm password again")
    return password1, password2
p1=""
p2=""
while True:
        print("set new password")
        p1,p2=getpa()
        if p1==p2 and 12>=len(p1)>=8:
            print("okay")
            break
print("password set")
