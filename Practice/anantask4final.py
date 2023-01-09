# from sys import argv
import string
special=string.ascii_lowercase
f=open(r"C:\Users\Shreyash Parajuli\Documents\LEV 4 SEM 1\FOCP\Practice\encrypt.txt","r")
decrypt=""
specials=["-","@","!","#","$","&","*","?"," ","_","\'"] 
# for key in range(0,ord("z")):
#     pass
for i in f.readlines():
    for j in i:
        if j in special:
            num=ord(j)+12
            if num > ord("z"):
                num=ord(j)-14
            decrypt+=chr(num)
        elif j in specials:
            decrypt+=j   
print(decrypt)