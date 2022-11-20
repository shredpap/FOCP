# Use an editor to input the Python program shown below then save it to a file called first_prog.py. Once that has been done, execute the program from the command line.

#Takes a string as input
number = input("Enter a number: ")
#converts the string to integer type value
number = int(number)
#prints out the user input
print("The numbered entered was", number)
#checks if the number is divisible by 2
if (number % 2) == 0:
	#prints out the statement if the condition was okay
	print("That is an even number")
	#runs when in-case the above condition was not met
	if (number%10)==0:
		print("That number is divisible by the number 10")
else:
	#prints out if the value is odd
	print("That is an odd number")
