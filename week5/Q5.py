# Last week you wrote a program that processed a collection of temperature readings
# entered by the user and displayed the maximum, minimum, and mean. Create a
# version of that program that takes the values from the command-line instead. Be
# sure to handle the case where no arguments are provided!
from sys import argv

a=[]
for i in argv[1:]:
    a.append(int(i))

print(f"Maximum is: {max(a)}\nMinimun is: {min(a)}\nSum     is: {sum(a)//len(a)}")