from random import randint as c
from rocknal import cal as p
cal=int(input("Rock,1/Paper,2/Scissors,3: "))
v=c(1,3)
user=p(cal)
comp=p(v)
print("you choose %s and computer choose %s" %(user, comp))
if cal!=v:
    if cal==1 or v==1 and cal!=2:
        if cal<v and (v!=2 or cal!=2):
            print("you win")
        else:
            print("you lose")
    elif cal>v:
        print("you win")
    else:
        print("you lose")
else:
    print("Draw")