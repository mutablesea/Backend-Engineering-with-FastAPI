name = input("What is your name?: ")

while True:
    try:
        age = int(input("What is your age?: "))
        break
    except ValueError:
        print("You must insert a valid number. Please type digits only.")
# print("Hello", name, "!", "Next year you will be", age + 1)
print(f"Hello {name}! Next year you will be {age + 1}.")

while True:
    try:
        birth_year = int(input("What is your birth year?: "))
        break
    except ValueError:
        print("You must insert a valid number. Please type digits only.")

if (2026 - birth_year) == age:
    print("Your Birthday hasn't come yet.")
else:
    print("Your Birthday has already passed.")
