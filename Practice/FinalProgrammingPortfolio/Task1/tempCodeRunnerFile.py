from random import choice
CONSTANTS=["literate","prickly","billowy","boat","kindly","lip","rainy","high-pitched","delightful","home","barbarous","chemical","gold","amusement","unhealthy","immense","rich","tacit","color","silly","scatter","idiotic","zip","guarded","faded","faint","ear","versed","admit","rings","aaron","ab","abandoned","abc","aberdeen","abilities","ability","able","aboriginal","abortion","about","above","abraham","abroad","abs","absence"]
# print(len(CONSTANTS))
s=set()
count=0
def pwd(c):
    '''Returns 3 random values as a string from a single list. '''
    a=""
    for i in range(3):
        temp=choice(c)
        a+=temp
    return a
try:
    times=int(input("Enter number of passwords to be generated: "))
    print("Password generator\n==================\n")
    if 0<times<25:  