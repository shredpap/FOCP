import random
a=[]
for i in range(10):
    a.append(i)
inp=int(input("are you feeling lucky? Enter a random number from 0-9"))
print(a)
temp=random.choice(a)
if temp==inp:
    print("you win")
else:
    print("you lose")
print(temp)
print(temp)
print(temp)
print(temp)