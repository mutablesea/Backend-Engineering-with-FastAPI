numbers = [2, 3, 7, 11, 13, 23, 31, 37, 41, 47, 53, 59, 61, 71, 73, 79, 97]

number = int(input("Guess a prime number(not all the prime number is in the list): "))

if number in numbers:
    print(f"Yes, Right guess. {number} Exists in my list")
else:
    print(f"No, Wrong guess. {number} Doesn't exist in my list")