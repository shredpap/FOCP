# Modify the previous program so that it can process any number of values. The input
# terminates when the user just pressed "Enter" at the prompt rather than entering a
# value.

a=[]
b=0
while True:
    d=input("Enter a number: ")
    if d!="":
        p=int(d)
        # print(type(p))
        a.append(p)
    else:
        break
print(max(a),min(a),sum(a)//len(a))