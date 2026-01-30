# calc function 


# add fucntion

def add(a,b):
    return a+b

def subtract(a,b):
    return a - b 

def multiply(a,b):
    return a * b

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Error cannot divide by 0 "

    

print("Welcome to the CLI Calculator!")

while True: 

    print("1:Add")
    print("2:Subtract")
    print("3:Multiply")
    print("4:Divide")
    print("5:Exit")
    
    choice = float(input("Please select an option:"))

    if choice == 5:
        print("Have a great day!")
        break

    try: 
        num1 = float(input("What is your first number?"))
        num2 = float(input("What is your second number?"))

    except ValueError:
    
        print("Please enter a valid number")
        continue 

    if choice == 1:
        total = add(num1,num2)
        print(f"Result:{total}")

    elif choice == 2: 
        total = subtract(num1,num2)
        print(f"Result:{total}")
    
    elif choice == 3:
        total = multiply(num1,num2)
        print(f"Result{total}")

    elif choice == 4:
        total = divide(num1,num2)
        print(f"Result:{total}")
    
    else:
        print("Invalid Menu choice ")
        





