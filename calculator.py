
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "I dont think you can do that smart guy"
    return a / b

print("Welcome... I guess. This is a calculator. Don’t get too excited. Also not quite sure why you cant do simple math.")

name = input("What’s your name? ...Not that I care: ")
print(f"Cool, {name}. Let’s just get this over with.")

num1 = float(input("First number, please... hurry up: "))
num2 = float(input("Second number... fine, type it: "))

print("Pick an operation. Options are: +, -, *, /")
operation = input("Which one do you want? ")

if operation == "+":
    result = add(num1, num2)
    print(f"Yeah, the answer is {result}. Happy now?")
elif operation == "-":
    result = subtract(num1, num2)
    print(f"Okay, it’s {result}. I could have done that in my head...")
elif operation == "*":
    result = multiply(num1, num2)
    print(f"Big surprise, it’s {result}. Whatever.")
elif operation == "/":
    result = divide(num1, num2)
    print(f"There. It’s {result}. You’re so welcome.")