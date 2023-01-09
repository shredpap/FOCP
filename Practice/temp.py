# total = 98.2
# count=5

# #add your extra code here
# avg=total/count
# print("The average is", avg)

#######################

# name=input("What's your name? \n")
# age=int(input("Enter your age? \n"))
# print(f"Hello There, {name} \n Your age is: \n Your name length is: {len(name)}")

#######################

# age=input("Enter your age ")
# age=int(age)
# print(f"in one year your age will be {age+1}")

#######################

# a,b=int(input("Enter first number: ")), int(input("Enter second number: "))
# print(a*b)

#######################

# comment="I would have"thought" you knew better!"
# print(comment)

#######################

# print("This test includes characters such as '\' '"' and "'",\n\tThis is a new line starts with a tab\n\t\tThis new line starts with two tabs")

#######################

# print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\nHello there!\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

#######################

# print("""This text spans three lines,
# and includes both single('),
# and double quotes(").""")

#######################

# surname="Palin"
# val=surname[:-1]
# print(val)

#######################

# primes=[2,3,5,7,13,17,19,23,29,31,37,41,43,47]
# sliced=primes[:4]
# print(sliced)

#######################

# names=['Barry', 'Michelle', 'Marin']
# name1,name2=input("Enter first name to add in list: "),input("Enter second name to add in list: ")
# names.insert(-1,name1)
# names.insert(-1,name2)
# print(names)

#######################

# import math
# print(math.sqrt(2401))

#######################

# from math import log2
# print(log2(1024))

#######################

# def displayTwice(msg):
#     """Fuction to print the message passed on the parameters"""
#     print(msg)
#     print(msg)
# displayTwice("One")
# displayTwice("Piece")
# help(displayTwice)

#######################

# def findMax(a,b):
#     """Finds the maximum of two values."""
#     if ( a > b ):
#         max = a
#     else:
#         max = b
#     return max
# findMax(1,2)
# findMax(15,99)
# findMax(10,15)

######################

# def multi(val1,val2=0):
#     if val2==0:
#         return val1**2
#     else:
#         return val1*val2
# print(multi(4,1))

######################

# def someFunc(x, y, z):
# 	print("x is", x, "\ny is", y, "\nz is", z)
# someFunc(y=10,x=3,z=33)
# someFunc(z=33,y=55,x=90)
# someFunc(12,13,14)

######################

# print("hello","!","jjj",sep="world")

######################

# def calcAve(*numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total/len(numbers)
# print(calcAve(1,2,3))
# print(calcAve(4,5,6))
# print(calcAve(10,20,30))
# print(calcAve(30,15,0))

######################

# to_seconds=lambda a,b=0 : (a*3600)+(b*60)
# print(to_seconds(1))
# print(to_seconds(2))

######################
# Introduction 
# Computer forensics aids in ensuring the integrity of digital evidence used in court cases in both the civil and criminal justice systems. Digital evidence, along with the forensic procedures used to gather, preserve, and investigate it, has grown in importance in helping to solve crimes and other legal matters as computers and other data-gathering tools are used more frequently in every aspect of life (DeVry University, n.d.).

# The majority of the data that modern devices gather are never visible to the average person. For instance, without the driver's knowledge, car computers continuously record information about when a driver shifts, brakes, and changes speed. Computer forensics frequently helps in locating and preserving this information because it can be crucial in resolving a legal dispute or a crime (Devry University, n.d.).

# Before we get into the report, let us clear the difference between Computer Forensics and Cybersecurity. Despite their shared interest in computer and criminals, they both serve a very different purpose (Devry University, n.d.).


# Section 1
# For computer forensics, the main focus is towards data recovery. Mostly the recovered data is used for trials in criminal cases, but also is for businesses when data is lost.
# Computer forensics ensures the integrity of digital evidence used in court cases in both the civil and criminal justice systems (Devry University, n.d.). 
# In this report we will be covering in the first section, what computer forensics is and how computer forensics team investigates. And in the second section we will be covering the topic cybersecurity, why is cybersecurity important, types of cybersecurity. After which we will be ending the report with some common real-life examples, and how to protect ourselves from cybercrime. 
# Even though both emphasize the safeguarding of information and digital assets. There are some major differences.
# To simply put it, Cybersecurity focuses on preventing cyberattacks and protecting organizations from them, while computer forensics is concerned with identifying and recovering data after a breach has occurred. Both fields are essential for ensuring the security of digital assets and information, and they rely on each other to provide ongoing protection for organizations (Krakoff, n.d.).
# Computer Forensics 
# Starting with computer forensics, it aids in ensuring the authenticity of digital evidence to be utilized in court cases and judicial systems, essentially data recovery (Devry University, n.d.).
# Computer forensics involves using specific techniques and tools to investigate digital devices for legal purposes. This includes analysing and preserving digital evidence from computers, mobile devices, and other digital media in a scientifically sound and court-admissible manner. (Devry University, n.d.).
# Computer forensics professionals may be needed to recover deleted or hidden files, trace the source of cyber-attacks, or examine the actions of computer users. They may also be responsible for creating reports and giving testimony in criminal and civil cases. (Devry University, n.d.).
# To conduct computer forensics, professionals need to be knowledgeable about computer systems, networks, and data storage, as well as relevant laws and legal procedures. They also need to be proficient in using specialized tools and techniques for analysing digital evidence, such as software to recover deleted files or hardware to analyse the contents of a hard drive. (Devry University, n.d.).
# Investigation
# Computer forensics is a crucial aspect of contemporary investigations. When a crime has been committed and an investigation is underway, investigators often look to the computer or phone of a suspect for clues. This is where a computer forensics expert comes in. Once a suspect has been identified and their computer or phone seized as evidence, a computer forensics specialist will search for data relevant to the investigation. To ensure that their findings can be used as evidence in court, they must follow strict protocols when collecting and analysing the data. The information they uncover, such as documents, browsing history, and metadata, may be used by prosecutors to build a strong case against the suspect(Devry University, n.d.).
# Section 2
# Cybersecurity
# Cybersecurity is the practice of protecting electronic devices, networks, and data from cyber threats such as hacking, theft, and damage. Cyberattacks, which can include malware, phishing scams, and ransomware, can have serious consequences on identity theft, financial loss, and damage to a company's reputation. To prevent cyberattacks, individuals and organizations should use strong passwords and security measures, keep their software and systems up to date, and be cautious when interacting with links or downloading files. It is also important to have a plan in place to respond to a potential cyberattack (Kaspersky, 2022).

# Why is it important
# The cybersecurity industry focuses on protecting devices and systems from attackers and their efforts have significant impacts. Without cybersecurity professionals, websites may be frequently disrupted by denial-of-service attacks and access to essential services such as power grids and water treatment facilities could be compromised. Without solid cybersecurity defences, these modern necessities could be easily destroyed. (Kaspersky, 2022).

# Types of Cybersecurity
# •	Network security is the practice of securing a computer network from intruders, whether targeted attackers or opportunistic malware (Kaspersky, 2022).
# •	Application security involves protecting software and devices from threats that may compromise the data they are designed to protect. It is essential to consider security in the design stage of a program or device to ensure that it is protected before it is deployed (Kaspersky, 2022).
# •	Information security ensures that data is kept safe and secure, whether it is being stored or transmitted, by protecting its integrity and confidentiality.
# •	Operational security involves protecting and managing data assets through processes and decisions related to access, storage, and sharing (Kaspersky, 2022).
# •	Disaster recovery and business continuity plans outline how an organization responds to and recovers from cybersecurity incidents or other disruptions to operations or data (Kaspersky, 2022). 
# •	End-user education teaches individuals good security practices to prevent accidental introduction of threats to secure systems (Kaspersky, 2022).

# Example of Indian call centre scam
# Scams originating from call centres in India often involve telemarketing or phishing calls targeted at people in other countries with the intention of stealing money or personal information. These scams can come in various forms, such as offering fake products or services, demanding payment for fake debts or fines, or attempting to obtain personal information for identity theft. Scammers may pose as representatives from reputable companies or government agencies to gain the trust of their victims. Indian call centre scams are hard to recognize and often result in financial losses for those affected. To avoid these scams, it is important to be wary of unsolicited phone calls, especially if they are from unknown numbers or individuals claiming to be from well-known organizations. Do not give out personal information or make payments over the phone unless you are certain you are dealing with a legitimate company or individual. Youtubers like Mark Rober, Kitboga, scambaiter, and Trilogy Media have played a significant role in exposing and catching scammers through their online content. These YouTubers create videos and other content that focus on identifying and confronting individuals or organizations that engage in fraudulent or deceptive practices. They use various methods, such as setting up sting operations and utilizing social engineering techniques, to uncover and expose scams. Through their content, these YouTubers aim to educate their audience about the tactics used by scammers and to help protect people from falling victim to scams. They have gained a large following online and have made a significant contribution to raising awareness about the issue of scamming.

# How to protect yourself
# There are several steps you can take to protect yourself from cybercrime:

# 1.	Use strong, unique passwords for each of your accounts. Avoid using the same password for multiple accounts (Johansen, 2020).

# 2.	Enable two-factor authentication (2FA) whenever possible. This adds an extra layer of security to your accounts by requiring you to enter a code sent to your phone or email in addition to your password (Johansen, 2020).

# 3.	Be careful what you click on. Don't click on links or download attachments from unknown sources, and be cautious even when the source seems trustworthy (Johansen, 2020).

# 4.	Keep your software and operating system up to date. Hackers often target vulnerabilities in outdated software, so it's important to make sure you have the latest security patches and updates (Johansen, 2020).

# 5.	Use a secure connection when accessing sensitive information online. Look for "https" at the beginning of the web address and a padlock icon to ensure the connection is secure (Johansen, 2020).

# Consider using a virtual private network (VPN) when accessing the internet over public Wi-Fi. This can help protect your data from being intercepted by hackers.

# Be aware of social engineering tactics. Hackers often use psychological manipulation to trick people into giving away sensitive information or taking actions that compromise their security.

# By following these tips, you can help protect yourself and your information from cybercriminals.













# Conclusion In conclusion, the fields of computer forensics and cybersecurity play a crucial role in safeguarding computer systems and information from harm, theft, and unauthorized use. Computer forensics involves the investigation and analysis of digital evidence for use in legal proceedings, and is crucial for solving cybercrimes and catching perpetrators. Cybersecurity, on the other hand, involves the implementation of measures such as strong passwords, locks, and firewalls to prevent cybercrimes from occurring in the first place. As technology and cybercrime continue to advance and evolve, it is vital to have strong capabilities in both computer forensics and cybersecurity to effectively combat these threats. Both are vital in today's digital age to protect individuals, organizations, and society as a whole from the risks and consequences of cybercrime. It is crucial for individuals and organizations to be aware of these issues and take steps to protect themselves, such as using strong passwords and security measures, keeping software and systems up to date, and being cautious when interacting with links or downloading files. By taking these precautions, individuals and organizations can better protect themselves and their assets from cyber threats. References•	Devry University, (n.d.) What is computer forensics? [Online]. Available from: <https://www.devry.edu/online-programs/area-of-study/technology/what-is-computer-forensics.html>  [Accessed on 6 January 2023].•	Johansen, A.G. (2020) 11 ways to help protect yourself against cybercrime [Online]. Available from: <https://us.norton.com/blog/how-to/how-to-recognize-and-protect-yourself-from-cybercrime> [Accessed on 6th January 2023]•	Kaspersky, (2022) What is cybersecurity? [Online]. Available from: <https://www.kaspersky.com/resource-center/definitions/what-is-cyber-security> [Accessed on 6 January 2023].
def decrypt_ceasar(ciphertext, shift):

    char_dict = {chr(i): chr(i) for i in range(65, 91)}
    char_dict.update({chr(i): chr(i) for i in range(97, 123)})
    result = ""
    for char in ciphertext:
# if the character is not a letter, just add it to the result string
        if char not in char_dict:
            result += char
            continue
        char_val = ord(char)

# if the character is uppercase
        if char_val in range(65, 91):
        # subtract the shift value and wrap around if necessary
            char_val -= shift
            if char_val < 65:
                char_val += 26
# if the character is lowercase
        elif char_val in range(97, 123):
  # subtract the shift value and wrap around if necessary
            char_val -= shift
            if char_val < 97:
                char_val += 26

# add the decrypted character to the result string
    result += char_dict[chr(char_val)]
    return result

ciphertext = "Vqrcyn Vzoy qw qivi dg pyboo qr Vzoy qw yvno dg pyboo qr qw qivi"
shift = 3
print(decrypt_ceasar("Bc cbs kcizr vojs pszwsjsr wb hvs zogh msofg ct hvs bwbshssbhv qsbhifm hvoh hvwg kcfzr kog pswbu kohqvsr yssbzm obr qzcgszm pm wbhszzwusbqsg ufsohsf hvob aob'g obr msh og acfhoz og vwg ckb; hvoh og asb pigwsr hvsagszjsg opcih hvswf jofwcig qcbqsfbg hvsm ksfs gqfihwbwgsr obr ghirwsr, dsfvodg ozacgh og boffckzm og o aob kwhv o awqfcgqcds awuvh gqfihwbwgs hvs hfobgwsbh qfsohifsg hvoh gkofa obr aizhwdzm wb o rfcd ct kohsf. Kwhv wbtwbwhs qcadzoqsbqm asb ksbh hc obr tfc cjsf hvwg uzcps opcih hvswf zwhhzs ottowfg, gsfsbs wb hvswf oggifobqs ct hvswf sadwfs cjsf aohhsf. Wh wg dcggwpzs hvoh hvs wbtigcfwo ibrsf hvs awqfcgqcds rc hvs goas. Bc cbs uojs o hvciuvh hc hvs czrsf kcfzrg ct gdoqs og gcifqsg ct viaob robusf, cf hvciuvh ct hvsa cbzm hc rwgawgg hvs wrso ct zwts idcb hvsa og wadcggwpzs cf wadfcpopzs. Wh wg qifwcig hc fsqozz gcas ct hvs asbhoz vopwhg ct hvcgs rsdofhsr romg. Oh acgh hsffsghfwoz asb tobqwsr hvsfs awuvh ps chvsf asb idcb Aofg, dsfvodg wbtsfwcf hc hvsagszjsg obr fsorm hc kszqcas o awggwcbofm sbhsfdfwgs. Msh oqfcgg hvs uizt ct gdoqs, awbrg hvoh ofs hc cif awbrg og cifg ofs hc hvcgs ct hvs psoghg hvoh dsfwgv, wbhszzsqhg jogh obr qccz obr ibgmadohvshwq, fsuofrsr hvwg sofhv kwhv sbjwcig smsg, obr gzckzm obr gifszm rfsk hvswf dzobg ouowbgh ig. Obr sofzm wb hvs hksbhwshv qsbhifm qoas hvs ufsoh rwgwzzigwcbasbh. ", 12)) # expected output: "This is a test of the ceasar cipher This is only a test of the ceasar cipher"
