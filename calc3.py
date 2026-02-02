
# calculator 

def add(a,b):
    return a + b 

def subtract(a,b):
    return a -b 

def multiply(a,b):
    return a * b 

def divide(a,b): 
    try: 
        return a/b
    except ZeroDivisionError: 
        return "Invalid cannot divide by 0"
    

print("Welcome to the CLI caluclator")

while True: 
    print("1)Addition")
    print("2)Subtraction")
    print("3)Mulitply")
    print("4)Divide")
    print("5)Exit")

    choice = int(input("Please choose an option 1-5"))
    if choice == 5:
        print("goodbye")
        break 
    try: 
        num1 = int(input("Please choose your first number"))
        num2 = int(input("Please enter the second number"))
    except ValueError: 
        print("Print a valid number please")


    if choice ==  1: 
        result = (add(num1,num2))
        print(f' Your result {result}')
    if choice ==  2: 
        result = (subtract(num1,num2))
        print(f' Your result {result}')
    if choice ==  3: 
        result = (multiply(num1,num2))
        print(f' Your result {result}')
    if choice ==  4: 
        result = (divide(num1,num2))
        print(f' Your result {result}')
