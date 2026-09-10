name = input("Enter your name: ")
while True:
    try:
        marks = int(input("Enter the marks: "))
        break
    except ValueError:
        print("Insert a valid number.")

# JavaScript / C / C++ / Java: Use if (marks < 0 || marks > 100)
# Python: uSe if marks < 0 or marks > 100: or if not (0 <= marks <= 100):
# nOt pOssIblE: if 0 > marks > 100
grade = ""
if marks < 0 or marks > 100:
    print("Invalid marks")
else:
    if marks >= 80:
        grade = "A+"
    elif marks >= 70:
        grade = "A"
    elif marks >= 60:
        grade = "A-"
    elif marks >= 50:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "F"

print(f"{name}, your grade is {grade}.")