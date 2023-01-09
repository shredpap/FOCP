import random,sys,string
aplh=[aplh for aplh in (string.ascii_lowercase+string.ascii_uppercase)]
try:
    f=(open(sys.argv[1],"r"))
    newfile=(open(r"C:\Users\Shreyash Parajuli\Documents\LEV 4 SEM 1\FOCP\FinalProgrammingPortfolio\Task3\Emails.txt","w"))
    email="@poppleton.ac.uk"
    def name(s):
        l = s.split()
        new = ""
        for i in range(len(l)):
            s = l[i]      
            new += (s[0]+'.')
        # new += l[-1].title()
        return new
    def nospe(special_string):    
        sample_list=[]
        for i in special_string:
            if i.isalnum():
                sample_list.append(i)
        normal_string="".join(sample_list)
        return normal_string
    for i in f.readlines():
        person=i[:-1]
        listp=person.split(",")
        inito=listp[1].lower()
        ini=name(inito)
        ids=listp[0].split()
        id=ids[0]
        lastname="".join(ids[1:])
        # inilist=[i for a,i in enumerate(lastname)]
        newfile.write(f"{id} {ini}{nospe(lastname.lower())}{(random.randint(1000,9999))}{email}\n")
        # lastname=[]
        # for val in lastlist:
        #     if val in aplh:
        #         lastname.append(val)
        # print("".join(map(str,lastname))
    # A string with special characters
    # special_string="spe@#$ci87al*&"
    # print("String before conversion: ",special_string)
    # Declaring a list
except FileNotFoundError as k:
    print("""Error: Cannot open "missing.txt". Sorry about that.""")
except IndexError:
    print("Error: Missing command-line argument.")
# f=(open(r"C:\Users\Shreyash Parajuli\Documents\LEV 4 SEM 1\FOCP\FinalProgrammingPortfolio\Task3\names.txt","r"))
