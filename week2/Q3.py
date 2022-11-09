# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is usually 24 students, but this is
# sometimes varied to create groups of similar size. Write a program that prompts for
# the number of students and group size, and then displays how many groups will be
# needed and how many will be left over in a smaller group.
# How many students? 113
# Required group size? 22
# There will be 5 groups with 3 students left over.
# For bonus credit, see if you can fix the grammar in the output. So if there were 101
# students in groups of 20 the output would be:
# There will be 5 groups with 1 student left over.
def leftover(stuin,gs):
    return stuin%gs
def grouper(stuin,gs):
    return stuin//gs
a=int(input("How many students? "))
b=int(input("Required group size? "))
group=grouper(a,b)
lefto=leftover(a,b)
if group>1 and lefto>1:
    print("There will be %d groups with %d students left over."%(group,lefto))
elif group>1:
    print("There will be %d groups with %d student left over."%(group,lefto))
elif lefto>1:
    print("There will be %d group with %d students left over."%(group,lefto))
else:
    print("There will be %d group with %d student left over."%(group,lefto))

