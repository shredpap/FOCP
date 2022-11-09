# Modify your greeting program so that if the user does not enter a name (i.e. they
# just press enter), the program responds "Hello, Stranger!". Otherwise it should print
# a greeting with their name as before.
name=input("enter a name: ")
if name=="":
    print("hello stranger")
else:
    print("hello",name)