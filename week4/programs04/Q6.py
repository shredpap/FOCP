# Write a program that takes a centigrade temperature and displays the equivalent in
# fahrenheit. The input should be a number followed by a letter C. The output should
# be in the same format.
from Q5 import c2f as c
def c2f(a):
    v=a[:-1]
    b=int(v)
    return (str(c(b))+"F")
# print(c2f("-40c"))