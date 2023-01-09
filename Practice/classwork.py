from random import choice as c
FIRSTWORD=["Apple","Chocolate","Bacon","Bagels","Burger","Cake","Coffee","Cookies","Donut","Cheese","Mango","Pizza","Grapes","Ice"]
SECONDWORD=["America","China","Colombia","France","Italy","Japan","Korea","Nepal"]
THIRDWORD=["Kai","Jayden","Ezra","Leo","Alex","Charlie","Elsa","Raya","Zoey","Ana","Mia","Kris","Kale","Nora","Rosa","Amy","May","June","Ray"]
print("Password Generator")
print("==================")
s=set()
while True:
    try:
        user=int(input("\nHow many passwords are needed? "))
        if (0< user <=2400):
            while len(s)!=user:
                pw=""
                pw+=c(FIRSTWORD).lower()+c(SECONDWORD).lower()+c(THIRDWORD).lower()
                s.add(pw)
            for i,j in range(user):
                print(f"{i} --> {j}")
        else:
            print("Please enter a value between 1 and 24.")
        break
    except ValueError:
        print("Please enter a number.")
print(len(s))