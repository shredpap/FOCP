from random import choice

def pwd(c):
    '''
    Returns 3 random values as a string from a single list.
    :parameter c: list of words
    :return: string of 3 randomly selected words from the list
    '''
    a = ""
    for i in range(3):
        temp = choice(c)
        a += temp
    return a

# List of words to be used for generating passwords
CONSTANTS = ["literate", "prickly", "billowy", "boat", "kindly", "lip", "rainy",
             "high-pitched", "delightful", "home", "barbarous", "chemical", "gold",
             "amusement", "unhealthy", "immense", "rich", "tacit", "color", "silly",
             "scatter", "idiotic", "zip", "guarded", "faded", "faint", "ear",
             "versed", "admit", "rings", "aaron", "ab", "abandoned", "abc",
             "aberdeen", "abilities", "ability", "able", "aboriginal", "abortion",
             "about", "above", "abraham", "abroad", "abs", "absence"]

s = set()
count = 0

# Prints the title of the program
print("Password generator\n==================\n")

while True:
    try:
        # user input for number of passwords to be generated
        times = int(input("Enter number of passwords to be generated: "))
        # check if number entered is between 1 and 24
        if 0 < times < 25:
            while len(s) != times:
                s.add(pwd(CONSTANTS))
            break
        else:
            print("Enter a number between 1 to 24.")
    except ValueError:
        print("Please enter a number. ")

# prints the generated passwords
for i in s:
    count += 1
    print(f'{count}--> {i}')
