name = "maggie" #this is a string
myAge = 428 #a integer
height = 5000.01 #this is a decimal number #a float/reel
hasAnOakSappling = True #a boolean (true/false question)

# casting (change from one data type to another)
age = input("enter age: ")
print(age)
print(age + "10") # concatenate 2 strings together (join them together)
ageAsAnInt = int(age)
print(ageAsAnInt + 10) # off two integers together (maths addition)
print("your age is " + str(ageAsAnInt))

stillAnInteger = -4
myNumber = "7984731791"

# arithmatic
add = 10 + 10
subtract = 10 - 10
multiply = 10 * 10
divide = 11 / 10 # will output a float
integerDivision = 10 // 10 
print(add, subtract, multiply, divide, integerDivision) 

modulo = 500 % 501 
print(modulo)
mystery = 2 ** 3 # to the power of 
print(mystery)

# activity 1 - take two inputs, multiply them together and output answer
number1 = input("enter a number: ") 
number2 = input("enter a number: ")
multiply = int(number1) * int(number2)
print(multiply)
print(number1 * number2)
# activity 2 - input users age, output age times 7

# activity 3 - take radius as input, output volume of sphere (v = 4/3 x pi x r^3)
radius = float(input("enter a radius: "))
print("volume of a sphere with radius ", radius, "is", 4/3 ** 3)
humanage = int(input("enter age"))
print("dog age is ", humanage * 7)