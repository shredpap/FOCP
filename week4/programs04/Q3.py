# Modify your "greetings" program so that the first letter of the name entered is
# always in uppercase with the rest in lowercase. This should happen even if the user
# entered their name differently. So if the user entered arthur, ARTHUR, or even
# arTHur the name should be displayed as Arthur
def firstcp(a):
    b=""
    for i in range(len(a)):
        if i==0:
            b+=a[i].upper()
        else:
            b+=a[i]
    return b
# print(firstcp("wertyui"))
