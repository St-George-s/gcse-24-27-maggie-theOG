passwordlength = 0
password = ""
lowercase_count = 0
uppercase_count = 0
specialcharacter_count = 0

print("input password: ")
password = input()
passwordlength = len(password)

print("is password longer than 8 characters?")
if passwordlength >= 8:
    print("yes, idiot")
else:
    print("no, idiot")

print("does password contain lowercase letters?")
for smth in password:
    if smth.islower():
        lowercase_count += 1
if lowercase_count > 0:
    print("you did it, you got lowercase letters in your password")
else:
    print("NOOOOOOOO why dont you have lowercase letters in your password")

print("does password contain uppercase letters?")
for smth in password:
    if smth.isupper():
        uppercase_count += 1
if uppercase_count > 0:
    print("yes you have uppercase letters in your password")
else:
    print("NOOO YOU NEED UPPERCASE LETTERS IN YOUR PASSWORD")

print("does password contain numbers?")
number_count = 0
for smth in password:
    if smth.isdigit():
        number_count += 1
if number_count > 0:
    print("yes, you have numbers in your password")
else:
    print("NOOOOO YOU NEED NUMBERS IN YOUR PASSWORD")

print("do you have special characters?")
specialcharacter_count = 0
for smth in password:
    if not smth.isalnum():
        specialcharacter_count += 1
if specialcharacter_count >= 1 :
    print("yep")
else:
    print("nop")


if passwordlength >= 8 and lowercase_count >= 1 and uppercase_count >= 1 and number_count >= 1:
    print("you did it, after ages you made a goddamn strong password")

else:
    print("password is not strong enough")
    if passwordlength < 8:
        print("YOU NEED TO MAKE YOUR PASS LONGER BROSKI")
    if lowercase_count == 0:
        print("dw just add a lowercase letter and sotp ragebaiting")
    if uppercase_count == 0:
        print("stop being a decomposing whale carcus and add uppercase letters")
    if number_count == 0:
        print("add numbers u dingus")

    
