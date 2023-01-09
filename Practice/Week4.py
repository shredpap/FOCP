#+12 if out of range -14
from sys import argv
from string import ascii_lowercase
import enchant 
d=enchant.Dict("en_US")
f=open(r"C:\Users\Shreyash Parajuli\Documents\LEV 4 SEM 1\FOCP\Practice\code.txt","r")
#lis=["1","2","3","4","5","6","7","8","9","0","!","?","."]
letters=((list(ascii_lowercase))+(list(ascii_lowercase)))
special=["-","@","!","#","$","&","*","?"," ","_","\'",".",",",";"] 
count=0
for key in range(len(letters)):
#     pass
        decrypt=""
        for i in f.readlines():
            for j in i:
                if j not in special:
                    num=letters.index(j.lower())+key
                    decrypt+=letters[num]
                else:
                    decrypt+=j  
                words=decrypt.split()
                for w in words:
                    if d.check(w):
                        count+=1
                if count==len(words):
                    print(decrypt)
                elif count==0:
                    print("Seems like it is not in ceaser cypher code")
# except FileNotFoundError:
#     pass
    #print(f"Error: Cannot open {sys.argv[1]}. Sorry about that.")