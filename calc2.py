
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b 

def multiply(a,b):
    return a * b

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Invalid: Cannot divide by 0"
    

print("Welcome to the calculator app")

while True: 

    print("1)ADD")
    print("2)Subtract")
    print("3)Mulitply")
    print("4)Divide")
    print("5)Exit")

    choice = int(input("Please choose an option 1 - 5"))

    if choice == 5: 
        print("Goodbye")
        break 

    try: 
        num1=float(input("What is your first number?"))
        num2=float(input("What is your second number?"))
    
    except ValueError:
        print("Invalid option: Please enter a number")

    if choice == 1: 
        result = add(num1,num2)
        print(f"Result{result}")

    elif choice == 2:
        result = subtract(num1,num2)
        print(f"Result:{result}")

    elif choice == 3:
        result = multiply(num1,num2)
        print(f"Result:{result}")
    
    elif choice == 4:
        result = divide(num1,num2)
        print(f"Result:{result}")
    else: 
        print("Invalid option: Please enter 1-5")
        

