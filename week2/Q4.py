# A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
# first count the sweets and then divide them according to how many pupils attend
# that day. Write a program that will tell the teacher how many sweets to give to each
# pupil, and how many she will have left over.
def leftover(stuin,gs):
    return stuin%gs
def grouper(stuin,gs):
    return stuin//gs
a=int(input("How many Sweets? "))
b=int(input("How many Pupils? "))
group=grouper(a,b)
lefto=leftover(a,b)
if group>1 and lefto>1:
    print("Each Pupil will get %d sweets with %d sweets left over."%(group,lefto))
elif group>1:
    print("Each Pupil will get %d sweets with %d sweet left over."%(group,lefto))
elif lefto>1:
    print("Each Pupil will get %d sweet with %d sweets left over."%(group,lefto))
else:
    print("Each Pupil will get %d sweet with %d sweet left over."%(group,lefto))