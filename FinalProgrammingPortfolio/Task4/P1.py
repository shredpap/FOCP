import string
import enchant
import random
import sys
from termcolor import colored

d = enchant.Dict("en_US")
alphabets = [alphabet for alphabet in (string.ascii_lowercase + string.ascii_uppercase)]

def decipher(inpt, shift_value):
    result = ""
    for i in range(len(inpt)):
        temp = inpt[i]
        if temp in alphabets:
            if temp.isupper():
                result += chr((ord(temp) + shift_value - 65) % 26 + 65)
            else:
                result += chr((ord(temp) + shift_value - 97) % 26 + 97)
        else:
            result += temp
    return result

try:
    with open(sys.argv[1], "r") as f:
        va = f.read()
except:
    print(colored("[ERROR] File not found", "red"))
    sys.exit(1)

fail = True
for i in range(26):
    count = 0
    temp12 = decipher(va, i)
    temp1 = temp12.split()
    ranlist = random.choices(temp1, k=4)
    for l in ranlist:
        if d.check(l):
            count += 1
    if count == 4:
        fail = False
        print(colored("Encrypted Text: ", "cyan"))
        print(va)
        print()
        print(colored("Decrypted Text: ", "cyan"))
        print(temp12)
        break

if fail:
    print(colored("Cannot decrypt. Most likely not a Caesar Cipher at work here.", "red"))
