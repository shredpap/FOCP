# A secret society has agreed on a password before potential new members are
# allowed into an online meeting. Write a program that prompts the user to enter a
# password. If it is correct, the user may join the meeting, otherwise they should be
# asked to re-enter. This should continue until the password is entered correctly. For
# example (the password here is obvious from the last line!):
# Greetings! What is the password? elderberry
# Incorrect! You may try again.
# Greetings! What is the password? hamster
# Incorrect! You may try again.
# Greetings! What is the password? parrot
# Correct! You may enter.
val=""
while val!="parrot":
    val=input("Greetings! What is the password? ")
    if val!="parrot":
        print("Incorrect! You may try again.")
    else:
        continue
print("Correct! You may enter.")