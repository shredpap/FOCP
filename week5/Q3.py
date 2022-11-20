# Write a program that takes a bunch of command-line arguments, and then prints
# out the shortest. If there is more than one of the shortest length, any will do.
# Hint: Don't overthink this. A good way to find the shortest is just to sort them.
from sys import argv
a=argv[1:]
# argv.append("hello")
a.sort(key=len)
print(a[0])
