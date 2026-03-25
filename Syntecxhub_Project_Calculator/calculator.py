# Syntecxhub Python Task 1 - Simple Calculator (Fixed)
print("🔥 SYNTECXHUB SIMPLE CALCULATOR 🔥")
print("=" * 40)

def get_numbers():
    """Get and validate two numbers"""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print(" Enter valid numbers!")

def calculate(num1, num2, operator):
    """Perform calculation"""
    if operator == '+': return num1 + num2
    elif operator == '-': return num1 - num2
    elif operator == '*': return num1 * num2
    elif operator == '/':
        if num2 == 0: return None
        return num1 / num2
    elif operator == 'c': return "clear"
    return "invalid"

def show_menu():
    """Show menu options"""
    print("\n📱 Operations:")
    print("1. + (Addition)")
    print("2. - (Subtraction)")
    print("3. * (Multiplication)")
    print("4. / (Division)")
    print("5. c (Clear)")
    print("6. Exit")

def main():
    """Main program loop"""
    while True:
        show_menu()
        choice = input("\nEnter choice (1-6 or +,-,*,/,c): ").strip()
        
        # Convert menu numbers to symbols
        if choice == '1': choice = '+'
        elif choice == '2': choice = '-'
        elif choice == '3': choice = '*'
        elif choice == '4': choice = '/'
        elif choice == '5': choice = 'c'
        elif choice == '6':
            print(" Thanks for using Syntecxhub Calculator!")
            break
        
        if choice in ['+', '-', '*', '/', 'c']:
            if choice == 'c':
                print(" Calculator cleared!")
                continue
            num1, num2 = get_numbers()
            result = calculate(num1, num2, choice)
            
            if result is None:
                print(" Division by Zero Error!")
            else:
                print(f" Result: {num1} {choice} {num2} = {result}")
        else:
            print(" Invalid choice! Use 1-6 or symbols.")

if __name__ == "__main__":
    main()
