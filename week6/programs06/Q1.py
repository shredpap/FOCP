# Write a function that accepts a positive integer as a parameter and then returns a
# representation of that number in binary (base 2).
val=int(input("Enter a number: "))
bins=lambda hello : bin(val).split("b")[1:]
print(bins(val))