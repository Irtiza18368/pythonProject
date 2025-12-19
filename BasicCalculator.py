def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

history = []
        
while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5. View History")
    print("6. Exit")

    selector = int(input("Select operation (1-6): "))

    if selector == 6:
        print("Goodbye")
        break

    if selector == 5:
        if not history:
            print("No calculations yet to show.")
        else:
            print("\nCalculation History:")
            for calculation in history:
                print(calculation)
        continue

    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    if selector == 1:
        result = add(number1, number2)
        record = f"{number1} + {number2} = {result}"

    elif selector == 2:
        result = subtract(number1, number2)
        record = f"{number1} - {number2} = {result}"

    elif selector == 3:
        result = multiply(number1, number2)
        record = f"{number1} * {number2} = {result}"

    elif selector == 4:
        if number2 == 0:
            print("Cannot divide by zero ")
            continue
        result = division(number1, number2)
        record = f"{number1} / {number2} = {result}"
    else:
        print("Invalid input")
        continue

    print("Result:", result)
    history.append(record)



