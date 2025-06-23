
def Celsius_to_Fahrenheit_Conversion(Current_Temperature):
    Fahrenheit = ((Current_Temperature * 9/5) + 32)
    print(Fahrenheit)


def Fahrenheit_to_Celsius_Conversion(Current_Temperature):
    Celsius = ((Current_Temperature - 32) * 5/9)
    print(Celsius)


def Main():
    Current_Temperature = float(input("What is the current temperature? "))
    
    Celsius_or_Fahrenheit = input("Did you enter the temperature in "
                                  "(c)elsius or (f)ahrenheit? ")
    
    if Celsius_or_Fahrenheit == 'c':
        Celsius_to_Fahrenheit_Conversion(Current_Temperature)
        
    elif Celsius_or_Fahrenheit == 'f':
        Fahrenheit_to_Celsius_Conversion(Current_Temperature)

    else:
        print("Invalid Input, try again with c or f")
        Main()


while True:
    Main()
    again = input("Do you want to convert another temperature? (yes or no): ")
    if again != 'yes':
        print("Goodbye!")
        break

#Jeremy Durdel
#Chapter 4 Lab 1
#06/23/2025
