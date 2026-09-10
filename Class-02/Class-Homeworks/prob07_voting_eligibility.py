while True:
    try:
        age = int(input("What is your age?: "))
        break
    except ValueError:
        print("Enter a valid number. Must enter a digit")

# strip() rEmoVe tHe 'Whitespace' bEtWeEn tHe sTriNg
while True:
    # ans = input("Are you a citizen of this country? (yes/no): ").strip().lower()
    ans = input("Are you a citizen of this country? (yes/no): ").lower()
    if ans in ['yes', 'y', 'true', '1']:
        is_citizen = True
        break
    elif ans in ['no', 'n', 'false', '0']:
        is_citizen = False
        break
    else:
        print("Enter a valid boolean value (yes/no).")

if age >= 18 and is_citizen:
    print("You are eligible for voting.")
else:
    print("You're not eligible for voting.")
