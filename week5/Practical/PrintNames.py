from sys import argv
if len(argv)>1:
    for i in argv[1:]:
        print(i)
else:
    print("No names provided")
