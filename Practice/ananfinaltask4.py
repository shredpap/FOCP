# from math import *
# def sr(a):
#     return a**0.5
#+12 if out of range -14
from sys import argv
from string import ascii_lowercase,ascii_uppercase
import enchant
print("Works..") 
# try:    
# f=open(argv[1],"r")
f="Bc cbs kcizr vojs pszwsjsr wb hvs zogh msofg ct hvs bwbshssbhv qsbhifm hvoh hvwg kcfzr kog pswbu kohqvsr yssbzm obr qzcgszm pm wbhszzwusbqsg ufsohsf hvob aob'g obr msh og acfhoz og vwg ckb; hvoh og asb pigwsr hvsagszjsg opcih hvswf jofwcig qcbqsfbg hvsm ksfs gqfihwbwgsr obr ghirwsr, dsfvodg ozacgh og boffckzm og o aob kwhv o awqfcgqcds awuvh gqfihwbwgs hvs hfobgwsbh qfsohifsg hvoh gkofa obr aizhwdzm wb o rfcd ct kohsf. Kwhv wbtwbwhs qcadzoqsbqm asb ksbh hc obr tfc cjsf hvwg uzcps opcih hvswf zwhhzs ottowfg, gsfsbs wb hvswf oggifobqs ct hvswf sadwfs cjsf aohhsf. Wh wg dcggwpzs hvoh hvs wbtigcfwo ibrsf hvs awqfcgqcds rc hvs goas. Bc cbs uojs o hvciuvh hc hvs czrsf kcfzrg ct gdoqs og gcifqsg ct viaob robusf, cf hvciuvh ct hvsa cbzm hc rwgawgg hvs wrso ct zwts idcb hvsa og wadcggwpzs cf wadfcpopzs. Wh wg qifwcig hc fsqozz gcas ct hvs asbhoz vopwhg ct hvcgs rsdofhsr romg. Oh acgh hsffsghfwoz asb tobqwsr hvsfs awuvh ps chvsf asb idcb Aofg, dsfvodg wbtsfwcf hc hvsagszjsg obr fsorm hc kszqcas o awggwcbofm sbhsfdfwgs. Msh oqfcgg hvs uizt ct gdoqs, awbrg hvoh ofs hc cif awbrg og cifg ofs hc hvcgs ct hvs psoghg hvoh dsfwgv, wbhszzsqhg jogh obr qccz obr ibgmadohvshwq, fsuofrsr hvwg sofhv kwhv sbjwcig smsg, obr gzckzm obr gifszm rfsk hvswf dzobg ouowbgh ig. Obr sofzm wb hvs hksbhwshv qsbhifm qoas hvs ufsoh rwgwzzigwcbasbh. "
d = enchant.Dict("en_US")
#lis=["1","2","3","4","5","6","7","8","9","0","!","?","."]
letters=((list(ascii_lowercase))+(list(ascii_uppercase)))
special=["-","@","!","#","$","&","*","?"," ","_","\'",".",",",";"] 
count=0
for key in range(len(letters)):
#     pass
    decrypt=""
    for i in f:
        for j in i:
            if j not in special:
                num=letters.index(j)+key
                decrypt+=letters[num]
            else:
                decrypt+=j  
    words=decrypt.split()
print(decrypt)
    