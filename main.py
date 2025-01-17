import calc

def main():
    while True:
        command = input("Enter add, sub, mult, div or 'stop' to exit: ").strip().lower()
        
        if command == "stop":
            break
        
        if command not in ["add", "sub", "mult", "div"]:
            print("Invalid command")
            continue
        
        try:
            num1 =int(input("Enter the first number: "))
            num2 =int(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        if command == "add":
            result = calc.add(num1, num2)
        elif command == "sub":
            result = calc.sub(num1, num2)
        elif command == "mult":
            result = calc.mult(num1, num2)
        elif command == "div":
            result = calc.div(num1, num2)
        
        print(result)
        
        another_operation = input("Would you like to perform another operation? yes or no: ").strip().lower()
        if another_operation != "yes":
            break

if __name__ == "__main__":
    main()
