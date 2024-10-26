#imports

#Building functions

def Disp_conversion_menu():
    
    print("Choose the temperature conversion type: ")
    print("1. Celcius(°C) to Fahrenheit(°F)")
    print("2. Celcius(°C) to Kelvin(°K)")
    print("3. Kelvin(°K) to Fahrenheit(°F)")
    print("4. Kelvin(°K) to Celcius(°C)")
    print("5. Fahrenheit(°F) to Celcius(°C)")
    print("6. Fahrenheit(°F) to Kelvin(°K)")
    
def temp_conversion():
    while True:
        Disp_conversion_menu()
        type_conv = input("Enter choice (1/2/3/4/5/6 or 'q' to quit: ")
        
        if type_conv == "q":
            print("Closing the Convertor")
            break
        
        
        if type_conv == "1":
            input_C = float(input("Enter Temperature value in Celcius: "))
            output_F = 32 + (9*input_C)/5
            print(f"Temperature in Fahrenheit is, {output_F}°F")
            
            
        if type_conv == "2":
            input_C = float(input("Enter Temperature value in Celcius: "))
            output_K = 273 + input_C
            print(f"Temperature in Kelvin is, {output_K}°K")
            
        
        if type_conv == "3":
            input_K = float(input("Enter Temperature value in Kelvin: "))
            output_F = 32 + (9*(input_K-273)/5)
            print(f"Temperature in Fahrenheit is, {output_F}°F")
            
        
        if type_conv == "4":
            input_K = float(input("Enter Temperature value in Kelvin: "))
            output_C = input_K - 273
            print(f"Temperature in Celcius is, {output_C}°C")
                 
        
        if type_conv == "5":
            input_F = float(input("Enter Temperature value in Fahrenheit: "))
            output_C = 5*(input_F-32)/9
            print(f"Temperature in Celcius is, {output_C}°C")
            
        
        if type_conv == "6":
            
            input_F = float(input("Enter Temperature value in Fahrenheit: "))
            output_K = 273 + (5*(input_F-32)/9)
            print(f"Temperature in Kelvin is, {output_K}°K")
            
            
#Run the Calculator
if __name__ == "__main__":
    temp_conversion()   
        