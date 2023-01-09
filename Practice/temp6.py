# a={}
# a={chr(i):i for i in range(ord('a'),ord('z')+1)}
# print(a)
# for i in range(ord('a'),ord('z')+1):
#     a[chr(i)]=i
# print(a)
# a="shred"
# p="ash"
# print(f"Hello {a} may i call you mr {p}")

# a=100_000_000
# b=500_000
# c=a*b
# print(f"{c:,}")

# *************************************
# val1="No one would have believed in the last years of the nineteenth century that"
# val2="Bc cbs kcizr vojs pszwsjsr wb hvs zogh msofg ct hvs bwbshssbhv qsbhifm hvoh"
# di=dict()
# for i in range(len(val1)):
#     if val1[i]!=" ":
#         di[val1[i]]=val2[i]
# print()

#**************************************

import string
from art import *
alphabets= [alphabets for alphabets in string.ascii_lowercase]
paragraph=list(input("Enter your list: ").lower())
shift_val=0
while True:
    for i in range(len(paragraph)):
        if paragraph[i] in alphabets:
            new=alphabets.index(paragraph[i])-shift_val
            paragraph[i]=alphabets[new]
    if shift_val==25:
        break
    shift_val+=1
    print("\n\n************************\n\n")
    tprint(f"{shift_val}")
    print("".join(map(str,paragraph)))
# paragraphs="Bc cbs kcizr vojs pszwsjsr wb hvs zogh msofg ct hvs bwbshssbhv qsbhifm hvohhvwg kcfzr kog pswbu kohqvsr yssbzm obr qzcgszm pm wbhszzwusbqsg ufsohsfhvob aob'g obr msh og acfhoz og vwg ckb; hvoh og asb pigwsr hvsagszjsg opcihhvswf jofwcig qcbqsfbg hvsm ksfs gqfihwbwgsr obr ghirwsr, dsfvodg ozacghog boffckzm og o aob kwhv o awqfcgqcds awuvh gqfihwbwgs hvs hfobgwsbhqfsohifsg hvoh gkofa obr aizhwdzm wb o rfcd ct kohsf. Kwhv wbtwbwhsqcadzoqsbqm asb ksbh hc obr tfc cjsf hvwg uzcps opcih hvswf zwhhzs ottowfg,gsfsbs wb hvswf oggifobqs ct hvswf sadwfs cjsf aohhsf. Wh wg dcggwpzshvoh hvs wbtigcfwo ibrsf hvs awqfcgqcds rc hvs goas. Bc cbs uojs o hvciuvhhc hvs czrsf kcfzrg ct gdoqs og gcifqsg ct viaob robusf, cf hvciuvh cthvsa cbzm hc rwgawgg hvs wrso ct zwts idcb hvsa og wadcggwpzs cfwadfcpopzs. Wh wg qifwcig hc fsqozz gcas ct hvs asbhoz vopwhg ct hvcgsrsdofhsr romg. Oh acgh hsffsghfwoz asb tobqwsr hvsfs awuvh ps chvsf asbidcb Aofg, dsfvodg wbtsfwcf hc hvsagszjsg obr fsorm hc kszqcas oawggwcbofm sbhsfdfwgs. Msh oqfcgg hvs uizt ct gdoqs, awbrg hvohofs hc cif awbrg og cifg ofs hc hvcgs ct hvs psoghg hvoh dsfwgv,wbhszzsqhg jogh obr qccz obr ibgmadohvshwq, fsuofrsr hvwg sofhv kwhv sbjwcigsmsg, obr gzckzm obr gifszm rfsk hvswf dzobg ouowbgh ig.Obr sofzm wb hvs hksbhwshv qsbhifm qoas hvs ufsoh rwgwzzigwcbasbh."