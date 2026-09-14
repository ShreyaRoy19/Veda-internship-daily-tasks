def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    if c < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
    return c + 273.15

def kelvin_to_celsius(k):
    if k < 0:
        raise ValueError("Temperature cannot be below absolute zero (0K).")
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return celsius_to_kelvin(fahrenheit_to_celsius(f))

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))


def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit & Kelvin")
    print("2. Fahrenheit to Celsius & Kelvin")
    print("3. Kelvin to Celsius & Fahrenheit")
    
    try:
        choice = int(input("Choose an option (1-3): "))
        if choice == 1:
            c = float(input("Enter temperature in Celsius: "))
            print(f"{c:.2f}°C = {celsius_to_fahrenheit(c):.2f}°F")
            print(f"{c:.2f}°C = {celsius_to_kelvin(c):.2f}K")
        elif choice == 2:
            f = float(input("Enter temperature in Fahrenheit: "))
            print(f"{f:.2f}°F = {fahrenheit_to_celsius(f):.2f}°C")
            print(f"{f:.2f}°F = {fahrenheit_to_kelvin(f):.2f}K")
        elif choice == 3:
            k = float(input("Enter temperature in Kelvin: "))
            print(f"{k:.2f}K = {kelvin_to_celsius(k):.2f}°C")
            print(f"{k:.2f}K = {kelvin_to_fahrenheit(k):.2f}°F")
        else:
            print("Invalid choice selected.")
    except (ValueError, ValueError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
