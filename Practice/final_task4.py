import string,enchant,random
from art import *
d = enchant.Dict("en_US")
alphabets= [alphabets for alphabets in (string.ascii_lowercase + string.ascii_uppercase)]
# print(alphabets)
def decipher(inpt,shift_value):
    result=""
    for i in range(len(inpt)):
        temp=inpt[i]
        if temp in alphabets:
            if (temp.isupper()):
                result+=chr((ord(temp)+shift_value-65)%26+65)
            else:
                result+=chr((ord(temp)+shift_value-97)%26+97)
        else:
            result+=temp
    return result
va="Esp Etxp Eclgpwwpc (qzc dz te htww mp nzygpytpye ez daplv zq stx) hld piazfyotyrl cpnzyotep xleepc ez fd. Std alwp rcpj pjpd dszyp lyo ehtyvwpo, lyo std fdflwwjalwp qlnp hld qwfdspo lyo lytxlepo. Esp qtcp mfcye mctrsewj, lyo esp dzqe clotlynpzq esp tynlyopdnpye wtrsed ty esp wtwtpd zq dtwgpc nlfrse esp mfmmwpd esle qwldspolyo alddpo ty zfc rwlddpd. Zfc nsltcd, mptyr std alepyed, pxmclnpo lyo nlcpddpo fdclespc esly dfmxteepo ez mp dle fazy, lyo espcp hld esle wfifctzfd lqepc-otyypclexzdaspcp, hspy eszfrse cfyd rclnpqfwwj qcpp zq esp eclxxpwd zq acpntdtzy. Lyosp afe te ez fd ty estd hlj - xlcvtyr esp aztyed htes l wply qzcpqtyrpc - ld hp dlelyo wlktwj loxtcpo std plcypdeypdd zgpc estd yph alclozi (ld hp eszfrse te)lyo std qpnfyotej."
for i in range(26):
    count=0
    temp12=decipher(va,i)
    temp1=temp12.split()
    ranlist=random.choices(temp1,k=4)
    for l in ranlist:
        # print(k)
        if d.check(l):
            count+=1
    if count==4:
        print(i)
        # print("".join(map(str,final)))
        print(temp12)
#         if count==4:
#             break
# if count==4:
#     tprint(f"{i}")
#     print(decipher(va,i))
# print(final)

