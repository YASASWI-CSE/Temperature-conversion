print("which type of conversion you want to perform?  " \
"\n1. Celsius to Fahrenheit  \n2. Fahrenheit to Celsius \n3. Celsius to Kelvin \n4. Kelvin to Celsius" \
"\n5. Fahrenheit to Kelvin \n6. Kelvin to Fahrenheit")
choice = int(input ("enter your choice:"))
match choice:
    case 1:
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C is equal to {f}°F")
    case 2:
        f = float(input("enter temperature in farenheit :"))
        c = (f - 32) * 5/9
        print(f"{f}°F is equal to {c}°C")
    case 3:
        c = float(input("Enter temperature in Celsius: "))
        k = c + 273.15
        print(f"{c}°C is equal to {k}K")
    case 4:
        k = float(input("Enter temperature in Kelvin: "))
        c = k - 273.15
        print(f"{k}K is equal to {c}°C")
    case 5:
        f = float(input("Enter temperature in Fahrenheit: "))
        k = (f - 32) * 5/9 + 273.15
        print(f"{f}°F is equal to {k}K")
    case 6:
        k = float(input("Enter temperature in Kelvin: "))
        f = (k - 273.15) * 9/5 + 32
        print(f"{k}K is equal to {f}°F")
    case _:
        print("Invalid choice. Please select a valid option.")
