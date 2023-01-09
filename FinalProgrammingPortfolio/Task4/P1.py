# import string,enchant,random
# from art import *
# d = enchant.Dict("en_US")
# alphabets= [alphabets for alphabets in string.ascii_lowercase]
# paragraph=list(input("Enter your list: ").lower())
# shift_val=0
# while True:
#     for i in range(len(paragraph)):
#         if paragraph[i] in alphabets:
#             new=alphabets.index(paragraph[i])-shift_val
#             paragraph[i]=alphabets[new]
#     if shift_val==25:
#         break
#     shift_val+=1
#     print("\n\n************************\n\n")
#     # rand_w=random.choices(paragraph, k=4)
#     # if d.check(random.choices(paragraph,k=4)):
#     tprint(f"{shift_val}")
#     # print(rand_w)
#     # print("".join(map(str,paragraph)))
#     maintemp="".join(map(str,paragraph))
#     lstt=maintemp.split()
#     rand_w=random.choices(paragraph, k=4)
#     print(rand_w)

# # paragraphs="Bc cbs kcizr vojs pszwsjsr wb hvs zogh msofg ct hvs bwbshssbhv qsbhifm hvohhvwg kcfzr kog pswbu kohqvsr yssbzm obr qzcgszm pm wbhszzwusbqsg ufsohsfhvob aob'g obr msh og acfhoz og vwg ckb; hvoh og asb pigwsr hvsagszjsg opcihhvswf jofwcig qcbqsfbg hvsm ksfs gqfihwbwgsr obr ghirwsr, dsfvodg ozacghog boffckzm og o aob kwhv o awqfcgqcds awuvh gqfihwbwgs hvs hfobgwsbhqfsohifsg hvoh gkofa obr aizhwdzm wb o rfcd ct kohsf. Kwhv wbtwbwhsqcadzoqsbqm asb ksbh hc obr tfc cjsf hvwg uzcps opcih hvswf zwhhzs ottowfg,gsfsbs wb hvswf oggifobqs ct hvswf sadwfs cjsf aohhsf. Wh wg dcggwpzshvoh hvs wbtigcfwo ibrsf hvs awqfcgqcds rc hvs goas. Bc cbs uojs o hvciuvhhc hvs czrsf kcfzrg ct gdoqs og gcifqsg ct viaob robusf, cf hvciuvh cthvsa cbzm hc rwgawgg hvs wrso ct zwts idcb hvsa og wadcggwpzs cfwadfcpopzs. Wh wg qifwcig hc fsqozz gcas ct hvs asbhoz vopwhg ct hvcgsrsdofhsr romg. Oh acgh hsffsghfwoz asb tobqwsr hvsfs awuvh ps chvsf asbidcb Aofg, dsfvodg wbtsfwcf hc hvsagszjsg obr fsorm hc kszqcas oawggwcbofm sbhsfdfwgs. Msh oqfcgg hvs uizt ct gdoqs, awbrg hvohofs hc cif awbrg og cifg ofs hc hvcgs ct hvs psoghg hvoh dsfwgv,wbhszzsqhg jogh obr qccz obr ibgmadohvshwq, fsuofrsr hvwg sofhv kwhv sbjwcigsmsg, obr gzckzm obr gifszm rfsk hvswf dzobg ouowbgh ig.Obr sofzm wb hvs hksbhwshv qsbhifm qoas hvs ufsoh rwgwzzigwcbasbh."
# va="Esp Etxp Eclgpwwpc (qzc dz te htww mp nzygpytpye ez daplv zq stx) hld piazfyotyrl cpnzyotep xleepc ez fd. Std alwp rcpj pjpd dszyp lyo ehtyvwpo, lyo std fdflwwjalwp qlnp hld qwfdspo lyo lytxlepo. Esp qtcp mfcye mctrsewj, lyo esp dzqe clotlynpzq esp tynlyopdnpye wtrsed ty esp wtwtpd zq dtwgpc nlfrse esp mfmmwpd esle qwldspolyo alddpo ty zfc rwlddpd. Zfc nsltcd, mptyr std alepyed, pxmclnpo lyo nlcpddpo fdclespc esly dfmxteepo ez mp dle fazy, lyo espcp hld esle wfifctzfd lqepc-otyypclexzdaspcp, hspy eszfrse cfyd rclnpqfwwj qcpp zq esp eclxxpwd zq acpntdtzy. Lyosp afe te ez fd ty estd hlj - xlcvtyr esp aztyed htes l wply qzcpqtyrpc - ld hp dlelyo wlktwj loxtcpo std plcypdeypdd zgpc estd yph alclozi (ld hp eszfrse te)lyo std qpnfyotej."
import string,enchant,random,sys,art
from art import *
d = enchant.Dict("en_US")
alphabets= [alphabets for alphabets in (string.ascii_lowercase + string.ascii_uppercase)]
def decipher(inpt,shift_value):
    """Takes in input and shift value to return the decrypted text."""
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
f=open(sys.argv[1],"r")
va=f.read()
for i in range(26):
    count=0
    temp12=decipher(va,i)
    temp1=temp12.split()
    ranlist=random.choices(temp1,k=4)
    for l in ranlist:
        if d.check(l):
            count+=1
    if count==4:
        tprint("Encrypted Text: ")
        print(va)
        tprint("Decrypted Text: ")
        print(temp12)







