"""Convert a temperature between Celsius and Fahrenheit."""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    choice = input("Convert from (C)elsius or (F)ahrenheit? ").strip().lower()
    try:
        value = float(input("Enter the temperature: "))
    except ValueError:
        print("Temperature must be a number.")
        return

    if choice == "c":
        print(f"{value:g}°C = {celsius_to_fahrenheit(value):.1f}°F")
    elif choice == "f":
        print(f"{value:g}°F = {fahrenheit_to_celsius(value):.1f}°C")
    else:
        print("Enter C or F.")

if __name__ == "__main__":
    main()
