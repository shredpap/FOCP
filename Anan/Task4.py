import re

def decrypt(ciphertext, shift):
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            shift %= 26
            if c.isupper():
                c = chr((ord(c) - shift - 65) % 26 + 65)
            else:
                c = chr((ord(c) - shift - 97) % 26 + 97)
        plaintext += c

    return plaintext

def is_english(text):
    count=0
    f=open(r"C:\Users\Shreyash Parajuli\Documents\LEV 4 SEM 1\FOCP\Anan\words.txt", "r")
    # English words that will be checked for in the decrypted text
    words=f.read().split("\n")
    # Check if any of the English words are in the text
    for word in words:
        if re.search(r"\b" + word + r"\b", text):
            count+=1
    if count>4:
        return True
    return False

ciphertext = "Bc cbs kcizr vojs pszwsjsr wb hvs zogh msofg ct hvs bwbshssbhv qsbhifm hvoh hvwg kcfzr kog pswbu kohqvsr yssbzm obr qzcgszm pm wbhszzwusbqsg ufsohsf hvob aob'g obr msh og acfhoz og vwg ckb; hvoh og asb pigwsr hvsagszjsg opcih hvswf jofwcig qcbqsfbg hvsm ksfs gqfihwbwgsr obr ghirwsr, dsfvodg ozacgh og boffckzm og o aob kwhv o awqfcgqcds awuvh gqfihwbwgs hvs hfobgwsbh qfsohifsg hvoh gkofa obr aizhwdzm wb o rfcd ct kohsf. Kwhv wbtwbwhs qcadzoqsbqm asb ksbh hc obr tfc cjsf hvwg uzcps opcih hvswf zwhhzs ottowfg, gsfsbs wb hvswf oggifobqs ct hvswf sadwfs cjsf aohhsf. Wh wg dcggwpzs hvoh hvs wbtigcfwo ibrsf hvs awqfcgqcds rc hvs goas. Bc cbs uojs o hvciuvh hc hvs czrsf kcfzrg ct gdoqs og gcifqsg ct viaob robusf, cf hvciuvh ct hvsa cbzm hc rwgawgg hvs wrso ct zwts idcb hvsa og wadcggwpzs cf wadfcpopzs. Wh wg qifwcig hc fsqozz gcas ct hvs asbhoz vopwhg ct hvcgs rsdofhsr romg. Oh acgh hsffsghfwoz asb tobqwsr hvsfs awuvh ps chvsf asb idcb Aofg, dsfvodg wbtsfwcf hc hvsagszjsg obr fsorm hc kszqcas o awggwcbofm sbhsfdfwgs. Msh oqfcgg hvs uizt ct gdoqs, awbrg hvoh ofs hc cif awbrg og cifg ofs hc hvcgs ct hvs psoghg hvoh dsfwgv, wbhszzsqhg jogh obr qccz obr ibgmadohvshwq, fsuofrsr hvwg sofhv kwhv sbjwcig smsg, obr gzckzm obr gifszm rfsk hvswf dzobg ouowbgh ig. Obr sofzm wb hvs hksbhwshv qsbhifm qoas hvs ufsoh rwgwzzigwcbasbh."
result="Answer not found"
for shift in range(26):
    decrypted_text = decrypt(ciphertext, shift)
    if is_english(decrypted_text):
        result=decrypted_text
        # print(f"Shift: {shift} => {decrypted_text}")
print(result)