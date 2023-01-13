import random
from sys import argv

# Open the "argv[1]" file for reading
file = open(argv[1], "r")
file.seek(0)

# Open the "emails.txt" file for writing
file1 = open(r"/Users/tanyaadhikari/Desktop/Final Project/emails.txt", "w")

list = []

# Loop to generate a list of random numbers between 1000 and 9999
for i in range(1000, 9999):
    list.append(i)

# Loop to get all the student names and id of the students
for i in file:
    # Split the line by "," and extract the student id number, first name, and last name
    total = i.split(",")
    Code = total[0].split(" ")
    last_name = Code[1].lower()
    Codes = Code[0]
    first_name = total[1]

    initials = ""
    #initializing the first letter of the first name
    for i in first_name:
        if i.isupper() == True:
            initials = initials + i + "."

    first_name = initials.lower()
    #pick a random number from the list
    number = random.choice(list)
    email = f"{Codes} {first_name}{last_name}{number}@poppleton.ec.uk\n"
    file1.write(email)

file1.close()
file.close()