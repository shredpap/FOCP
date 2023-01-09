import random,sys,string
aplh=[aplh for aplh in (string.ascii_lowercase+string.ascii_uppercase)]
f=(open(r"C:\Users\Shreyash Parajuli\Documents\LEV 4 SEM 1\FOCP\FinalProgrammingPortfolio\Task3\names.txt","r"))
def name(s):
    l = s.split()
    new = ""
    for i in range(len(l)):
        s = l[i]      
        new += (s[0]+'.')      
    # new += l[-1].title()
    return new
for i in f.readlines():
    person=i[:-1]
    listp=person.split(",")
    inito=listp[1].lower()
    ini=name(inito)
    ids=listp[0].split()
    id=ids[0]
    lastname="".join(ids[1:])
    lastlist=[i for a,i in enumerate(lastname)]
    print(lastname)
    # final=id+" "+ini+
    # lastname=[]
    # for val in lastlist:
    #     if val in aplh:
    #         lastname.append(val)
    # print("".join(map(str,lastname)))