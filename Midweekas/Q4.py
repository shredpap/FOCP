def password_checker(password):
    from string import ascii_letters as letters, digits, punctuation
    has_letter = has_digit = has_punc = False
    for character in password:
        if character in letters:
            has_letter = True
        elif character in digits:
            has_digit = True
        elif character in punctuation:
            has_punc = True
    return has_letter and has_digit and has_punc
# print(password_checker("Nasdjhfadf@999"))
import time
while True:
    pwd=input("Enter your password ")
    pwd2=input("Confirm your password ")
    if pwd==pwd2 and password_checker(pwd)==True:
        print("Password has been set!")
        break
    else:
        print("Invalid password, please try again! in 10 seconds")
        time.sleep(10)
