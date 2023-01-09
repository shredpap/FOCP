# A cafe offers a menu consisting solely of eggs and spam. A diner always gets one
# egg, but may choose how much spam they would like. They must have at least one
# slice. Write a program that displays the correct name of their chosen dish, like so:
# How many slices of spam? 3
# Egg with Spam, Spam, and Spam coming up!
# How many slices of spam? 1
# Egg with Spam coming up!
num=int(input("How many slices of spam? "))
sp="Spam"
if num>1:
    for i in range(num-2): 
        sp+=", Spam"
    print(f"Egg with {sp} and Spam coming up!")
else:
    print("Egg with Spam coming up!")