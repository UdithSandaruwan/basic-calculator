def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("float division by zero")
        return None
    return a / b

def power(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error: Modulo by zero")
        return None
    return a % b

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    if choice == '#':
        print("#\nDone. Terminating\n")
        break
    elif choice == '+':
        print(choice)
        a = input("Enter first number: ")
        if  a == "0$":
            print(a)
            continue
        elif a == '#':
            print("#\nDone. Terminating\n")
            break
        else:
            a = float(a)
            print(int(a)) 
        b = input("Enter second number: ")
        if b == "0$":
            print(b)
            continue
        elif b == '#':
            print("#\nDone. Terminating\n")
            break
        else:
            b = float(b)
            print(int(b)) 
        result = add(a, b)
        print(f"{a} + {b} = {result}")
        
        
    elif choice == '-':
        print(choice)
        a = input("Enter first number: ")
        if  a == "0$":
            print(a)
            continue
        elif a == '#':
            print("#\nDone. Terminating\n")
            break
        else:
            a = float(a)
            print(int(a)) 
        b = input("Enter second number: ")
        if  b == "0$":
            print(b)
            continue
        elif b == '#':
            print("#\nDone. Terminating\n")
            break
        else:
            b = float(b)
            print(int(b)) 
        result = subtract(a, b)
        print(f"{a} - {b} = {result}")
    elif choice == '*':
        print(choice)
        a = input("Enter first number: ")
        if  a == "0$":
            print(a)
            continue
        elif a == '#':
            print("#\nDone. Terminating\n")
            break
        else:
            a = float(a)
            print(int(a)) 
        b = input("Enter second number: ")
        if  b == "0$":
            print(b)
            continue
        elif b == '#':
            print("#\nDone. Terminating\n")
            break
        else:
            b = float(b)
            print(int(b)) 
        result = multiply(a, b)
        print(f"{a} * {b} = {result}")
    elif choice == '/':
        print(choice)
        a = input("Enter first number: ")
        if  a == "0$":
            print(a)
            continue
        elif a == '#':
            print("#\nDone. Terminating\n")
            break
        else:
            a = float(a)
            print(int(a)) 
        
        b = input("Enter second number: ")
        if b == "0$":
            print(b)
            continue
        elif b == '#':
            print("#\nDone. Terminating\n")
            break
        else:
            b = float(b)
            print(int(b)) 
        
        if a == 0 and b == 0:
            print("Both numbers are zero. Undefined result.")
        else:
            result = divide(a, b)
            print(f"{a} / {b} = {result}")
    elif choice == '^':
        print(choice)
        a = input("Enter base: ")
        if  a == "0$":
            print(a)
            continue
        elif a == '#':
            print("#\nDone. Terminating\n")
            break
        else:
            a = float(a)
            print(int(a)) 
        b = input("Enter exponent: ")
        if  b == "0$":
            print(b)
            continue
        elif b == '#':
            print("#\nDone. Terminating\n")
            break
        else:
            b = float(b)
            print(int(b)) 
        result = power(a, b)
        print(f"{a} ^ {b} = {result}")
    elif choice == '%':
        print(choice)
        a = input("Enter dividend: ")
        if  a == "0$":
            print(a)
            continue
        elif a == '#':
            print("#\nDone. Terminating\n")
            break
        else:
            a = float(a)
            print(int(a)) 
        b = input("Enter divisor: ")
        if  b == "0$":
            print(b)
            continue
        elif b == '#':
            print("#\nDone. Terminating\n")
            break
        else:
            b = float(b)
            print(int(b)) 
        result = remainder(a, b)
        print(f"{a} % {b} = {result}")
    elif choice == '$':
        print("Resetting...")
        continue
    else:
        print("Unrecognized operation")
