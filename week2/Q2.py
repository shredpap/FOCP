# Write a program that prompts a user to enter a temperature in Celsius, and then
# displays the corresponding temperature in Fahrenheit, like so:
# Enter a temperature in Celsius: 32.5
# 32.5C is equivalent to 90.5F.

def temp(val):
    far=(val * (9/5)) + 32
    return far

cel=float(input("Enter a temperature in Celsius: "))
outp=temp(cel)
print("%.2f is equivalent to %.2f"%(cel,outp))