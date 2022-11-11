# When processing data it is often useful to remove the last character from some
# input (it is often a newline). Write and test a function that takes a string parameter
# and returns it with the last character removed. (If the string contains one or fewer
# characters, return it unchanged.)
def rlast(a):
    b=""
    for i in range(len(a)):
        if len(a)>1:
            if i==len(a)-1:
                break
            else:
                b+=a[i]
        else:
            b+=a[i]
    return b
print(rlast("wdgad"))