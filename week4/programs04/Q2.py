# Write a function that has a single string as its parameter, and returns the number of
# uppercase letters, and the number of lowercase letters in the string. Test the
# function with a short program.
def countchr(a):
    lowcnt=0
    upcnt=0
    for i in a:
        if (i.islower()):
            lowcnt+=1
        elif i!=" ":
            upcnt+=1
    return lowcnt, upcnt
a,b=countchr("hello HELLO")
print(a,"is the number of lower letters",b,"is the number of upper letters")