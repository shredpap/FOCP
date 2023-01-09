from random import choice
CONSTANTS=["literate","prickly","billowy","boat","kindly","lip","rainy","high-pitched","delightful","home","barbarous","chemical","gold","amusement","unhealthy","immense","rich","tacit","color","silly","scatter","idiotic","zip","guarded","faded","faint","ear","versed","admit","rings","aaron","ab","abandoned","abc","aberdeen","abilities","ability","able","aboriginal","abortion","about","above","abraham","abroad","abs","absence","absent","absolute","absolutely","absorption","abstract","abstracts","abu","abuse","ac","academic","academics","academy","acc","accent","accept","acceptable","acceptance","accepted","accepting","accepts","access","accessed","accessibility","accessible","accessing","accessories","accessory","accident","accidents","accommodate","accommodation","accommodations","accompanied","accompanying","accomplish","accomplished","accordance","according","accordingly","account","accountability","accounting","accounts","accreditation","accredited","accuracy","accurate","accurately","accused","acdbentity","ace","acer","achieve","achieved","achievement","achievements","achieving","acid","acids","acknowledge","acknowledged","acm","acne","acoustic","acquire","acquired","acquisition","acquisitions","acre","acres","acrobat","across","acrylic","act","acting","action","actions","activated","activation","active","actively","activists","activities","activity","actor","actors","actress","acts","actual","actually","acute","ad","ada","adam","adams","adaptation","adapted","adapter","adapters","adaptive","adaptor","add","added","addiction","adding","addition","additional","additionally","additions","address","addressed","addresses","addressing","adds","adelaide","adequate","adidas","adipex","adjacent","adjust","adjustable","adjusted","adjustment","adjustments","admin","administered","administration","administrative","administrator","administrators","admission","admissions","admit","admitted"]
# print(len(CONSTANTS))
s=set()
def pwd(c):
    '''Returns 3 random values as a string from a single list. '''
    a=""
    for i in range(3):
        temp=choice(c)
        a+=temp
    return a
try:
    times=int(input("Enter number of passwords to be generated: "))
    print("Password generator\n==================\n")
    if 0<times<2500:    
        for i in range(times):
            print(f'{i+1}--> {pwd(CONSTANTS)}')
            s.add(pwd(CONSTANTS))
    else:
        print("Enter a number between 1 to 24.")
except ValueError:
    print("Please enter a number. ")


print(len(s))

