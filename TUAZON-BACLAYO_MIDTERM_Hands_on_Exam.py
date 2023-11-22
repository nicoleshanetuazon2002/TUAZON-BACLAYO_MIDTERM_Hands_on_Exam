import random

num1 = random.randint(1,99)
num2 = random.randint(1,99)

print("what is the sum of", num1, "+", num2, "?")
variable = eval(input("Enter Answer here:"))
ans = num1+num2
if variable == ans:
    print("Your answer is correct!")

elif variable != ans:
    print("Incorrect!")

print("what is the sum of", num1, "-", num2, "?")
variable = eval(input("Enter Answer here:"))
ans = num1-num2
if variable == ans:
    print("Your answer is correct!")

elif variable != ans:
    print("Incorrect!")

print("what is the sum of", num1, "x", num2, "?")
variable = eval(input("Enter Answer here:"))
ans = num1*num2
if variable == ans:
    print("Your answer is correct!")

elif variable != ans:
    print("Incorrect!")

print("what is the sum of", num1, "/", num2, "?")
variable = eval(input("Enter Answer here:"))
ans = num1/num2
if variable == ans:
    print("Your answer is correct!")

elif variable != ans:
    print("Incorrect!")