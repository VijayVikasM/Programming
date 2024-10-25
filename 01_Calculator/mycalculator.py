#There are three versions of Calculators in this project
#01 Basic Arithemtic level calculator (based on user input in terminal (No GUI))
#02 Basic Arithemtic level calculator (With GUI)
#03 Basic Scientific Calculator (With GUI)


#Defining the arithmetic functions
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Invalid! Division by Zero!"
    else:
        return a / b
    
#Display Menu Options

def display_menu():
    print("Select operation based on the codes given below: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
#Calculator main function

def calculator():
    while True:
        display_menu()
        choice = input("Enter choice (1/2/3/4 or 'q' to quit: ")
        
        if choice == "q":
            print("Closing the Calculator")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue
            
            #Perform individual operations based on choice
            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
        else:
            print("Invalid choice! Please choose a valid operation.")
            
            
#Run the Calculator
if __name__ == "__main__":
    calculator()