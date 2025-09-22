def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b        
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def power(a, b):
    return a ** b
def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return a ** 0.5

print("Welcome to Calculator App")
while True:
    print("Select operation:")
    print("1. Add")         
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Exit")
    choice = input("Enter choice(1/2/3/4/5/6/7): ")
    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                print(e)
        elif choice == '5':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
    elif choice == '6':
        num = float(input("Enter number: "))
        try:
            print(f"√{num} = {sqrt(num)}")
        except ValueError as e:
            print(e)
    elif choice == '7':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid input")