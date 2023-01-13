import random
import sys

def generate_email(first_name, last_name, id_number):
    """
    Generates an email address using the first name, last name, and id number of a person
    :param first_name: first name of the person
    :param last_name: last name of the person
    :param id_number: id number of the person
    :return: email address
    """
    # convert the first name to initials
    initial = '.'.join([name[0] for name in first_name.split()])
    # remove non-alphanumeric characters from last name and convert to lowercase
    last_name = ''.join(char for char in last_name if char.isalnum()).lower()
    # generate the email address
    email = f"{id_number}: {initial}.{last_name}{random.randint(1000, 9999)}@poppleton.ac.uk"
    return email

try:
    # get the file name from the command-line argument
    file_name = sys.argv[1]
    # open the file and the new file to write the emails
    with open(file_name, "r") as f, open("Emails.txt", "w") as new_file:
        for line in f:
            # split the line into the person's information
            person = line.strip().split(',')
            # get the id number, first name, and last name
            id_number = person[0].split()[0]
            first_name = person[1].lower()
            last_name = ' '.join(person[0].split()[1:]).lower()
            # generate the email address
            email = generate_email(first_name, last_name, id_number)
            # write the email address to the new file
            new_file.write(f"{email}\n")
except FileNotFoundError:
    print("Error: Cannot open the specified file. Please check the file name and try again.")
except IndexError:
    print("Error: Missing command-line argument.")
except:
    print("Error: An unknown error occurred.")
