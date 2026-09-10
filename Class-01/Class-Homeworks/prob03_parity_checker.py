while True:
    try:
        whole_number = int(input("Enter any Whole number: "))
        break
    except ValueError:
        print("You must insert a valid number. Please type digits only.")
'''
if whole_number < 0:
    print("Are you a dumb? Negative number is not a whole number.")
    whole_number = int(input("Enter the Whole number: "))
elif whole_number % 1 != 0:
    print("you are really a dumb. Fraction number is not a whole number.")
    whole_number = int(input("Enter the Whole number: "))
'''

print(whole_number % 2 == 0)

if whole_number % 2 == 0:
    print(f"The given Whole number {whole_number} is Even.")
else:
    print(f"The given Whole number {whole_number} is Odd.")