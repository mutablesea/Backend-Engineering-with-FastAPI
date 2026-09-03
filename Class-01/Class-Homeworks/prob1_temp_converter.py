while True:
    try:
        celsius_value = float(input("What is the Temperature today(Celsius)?: "))
        break
    except ValueError:
        print("You must insert a valid number. Please type digits only.")

fahrenheit_value = celsius_value * (9/5) + 32
print(f"The Temperature is {fahrenheit_value}F.")

# aFtEr tWo dEcImaL dIgIt
# print(f"The Temperature is {fahrenheit_value:.2f}F.")

# rOunD tHe vAluE
# print(f"The Temperature is {round(fahrenheit_value, 2)}F.")

