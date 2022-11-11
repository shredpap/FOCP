# Write and test a function that converts a temperature measured in degrees
# centigrade into the equivalent in fahrenheit, and another that does the reverse
# conversion. Test both functions. (Google will find you the formulae) (0°C × 9/5) + 32 = 32°F || (32°F − 32) × 5/9
def c2f(a):
    return (a*(9/5))+32
def f2c(a):
    return ((a-32)*(5/9))

