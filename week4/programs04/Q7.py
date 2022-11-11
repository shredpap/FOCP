# Write a program that reads 6 temperatures (in the same format as before), and
# displays the maximum, minimum, and mean of the values
# from Q6 import c2f as c

a=[]
# k=[]
for i in range(6):
        a.append(int(input("Enter a number: ")))
def mms(a):
    return max(a),min(a),sum(a)//6
print(mms(a))
# for j in a:
#     k.append(c(j))
# print(max(k),min(k),sum(k)//6)