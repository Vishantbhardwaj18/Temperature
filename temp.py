# Temperature Converter Application

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def temperature_converter():
    print("Welcome to the Temperature Converter!")
    print("Select conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    while True:
        choice = input("\nEnter choice (1/2/3/4/5/6/7): ")

        if choice in ['1', '2', '3', '4', '5', '6']:
            temp = float(input("Enter the temperature value: "))

            if choice == '1':
                print(f"{temp}°C is {celsius_to_fahrenheit(temp)}°F")
            elif choice == '2':
                print(f"{temp}°C is {celsius_to_kelvin(temp)}K")
            elif choice == '3':
                print(f"{temp}°F is {fahrenheit_to_celsius(temp)}°C")
            elif choice == '4':
                print(f"{temp}°F is {fahrenheit_to_kelvin(temp)}K")
            elif choice == '5':
                print(f"{temp}K is {kelvin_to_celsius(temp)}°C")
            elif choice == '6':
                print(f"{temp}K is {kelvin_to_fahrenheit(temp)}°F")
        elif choice == '7':
            print("Exiting the Temperature Converter. Goodbye!")
            break
        else:
            print("Invalid input! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    temperature_converter()
