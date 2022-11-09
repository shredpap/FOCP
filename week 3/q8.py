intput=int(input("Enter a number"))
if intput>0:
    for i in range(13):
        print(i,"x",intput,"=",i*intput)
else:
    for i in reversed(range(13)):
        print(i,"x",intput,"=",i*intput)