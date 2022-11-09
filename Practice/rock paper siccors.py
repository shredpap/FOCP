from random import randint as c
cal=int(input("Rock,1/Paper,2/Scissors,3: "))
v=c(1,3)
if cal!=v:
    if cal==1 or v==1 and cal!=2:
        if cal<v and (v!=2 or cal!=2):
            print("you win",cal,v)
        else:
            print("you lose",cal,v)
    elif cal>v:
        print("you win",cal,v)
    else:
        print("you lose",cal,v)
else:
    print("Draw",cal,v)