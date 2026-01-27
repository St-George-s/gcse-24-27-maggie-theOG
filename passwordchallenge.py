passwordlength = 0
password = ""
lowercase_count = 0
uppercase_count = 0


print("input password: ")
password = input()
passwordlength = len(password)


if passwordlength >= 8:
    print("✅")
else:
    print("❌")


for smth in password:
    if smth.islower():
        lowercase_count += 1
if lowercase_count > 0:
    print("✅")
else:
    print("❌")


for smth in password:
    if smth.isupper():
        uppercase_count += 1
if uppercase_count > 0:
    print("✅")
else:
    print("❌")


number_count = 0
for smth in password:
    if smth.isdigit():
        number_count += 1
if number_count > 0:
    print("✅")
else:
    print("❌")

print("this is yout final result:")


if passwordlength >= 8 and lowercase_count >= 1 and uppercase_count >= 1 and number_count >= 1:
    print("you did it, after ages you made a goddamn strong password")

if passwordlength >=8 and lowercase_count >= 1 and uppercase_count >= 1 and number_count == 0:
    print("not good enough")

if passwordlength >= 8 and lowercase_count >= 1 and uppercase_count == 0 and number_count >= 0:
    print("not good enough")

if passwordlength >= 8 and lowercase_count == 0 and uppercase_count >= 1 and number_count >= 1:
    print("not good enough")

if passwordlength <8 and lowercase_count >= 1 and uppercase_count >= 1 and number_count >= 1:
    print("not good enough")

if passwordlength <8 and lowercase_count == 0 and uppercase_count >= 1 and number_count >= 1:
    print("not good enough")

if passwordlength <8 and lowercase_count >= 1 and uppercase_count == 0 and number_count >= 1:
    print("not good enough")

if passwordlength <8 and lowercase_count >= 1 and uppercase_count >= 1 and number_count == 0:
    print("not good enough")

if passwordlength >=8 and lowercase_count == 0 and uppercase_count == 0 and number_count >= 1:
    print("not good enough")

if passwordlength >=8 and lowercase_count == 0 and uppercase_count >= 1 and number_count == 0:
    print("not good enough")

if passwordlength >=8 and lowercase_count >= 1 and uppercase_count == 0 and number_count == 0:
    print("not good enough") 

if passwordlength <8 and lowercase_count == 0 and uppercase_count == 0 and number_count >= 1:
    print("not good enough") 

if passwordlength <8 and lowercase_count == 0 and uppercase_count >= 1 and number_count == 0:
    print("not good enough")

if passwordlength <8 and lowercase_count >= 1 and uppercase_count == 0 and number_count == 0:
    print("not good enough")

if passwordlength >= 8 and lowercase_count == 0 and uppercase_count == 0 and number_count == 0:
    print("not good enough")




    
