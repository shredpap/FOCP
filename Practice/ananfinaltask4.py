import string,random,enchant,sys
d=enchant.Dict("en_US")
def decipher_caesar(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr((ord(char) - shift - 65) % 26 + 65)
                plaintext += shifted_char
            else:
                shifted_char = chr((ord(char) - shift - 97) % 26 + 97)
                plaintext += shifted_char
        else:
            plaintext += char
    return plaintext
f=open(sys.argv[1],"r").read()
for shift_value in range(26):
    count=0

    decry=decipher_caesar(f,shift_value)
    decryls=decry.split()
    randomwords=random.choices(decryls,k=4)
    for val in randomwords:
        if d.check(val):
            count+=1
        if count==4:
            print(decry)