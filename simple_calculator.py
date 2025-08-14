def calculator():
    """Simple command-line calculator"""
    print("🧮 Simple Python Calculator")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit")
    print("-" * 30)
    
    while True:
        try:
            # Get first number
            num1 = input("Enter first number: ")
            if num1.lower() == 'quit':
                break
            
            num1 = float(num1)
            
            # Get operation
            operation = input("Enter operation (+,-,*,/): ")
            if operation.lower() == 'quit':
                break
            
            # Get second number
            num2 = input("Enter second number: ")
            if num2.lower() == 'quit':
                break
            
            num2 = float(num2)
            
            # Perform calculation
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("❌ Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
            else:
                print("❌ Invalid operation! Use +, -, *, or /")
                continue
            
            # Display result
            print(f"✅ Result: {num1} {operation} {num2} = {result}")
            print("-" * 30)
            
        except ValueError:
            print("❌ Error: Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break

if __name__ == "__main__":
    calculator() 