numbers_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
numbers = [11, 22, 33, 44, 55]
a = [1, 2, 3, 4, 5]
print(numbers_list)
print(type(numbers_list))

print(f"The 'First' number on the list is {numbers_list[0]}")
print(f"The 'Second' number on the list is {numbers_list[1]}")
print(f"The 'Last' number on the list is {numbers_list[-1]}")
print(f"The 'Second Last' number on the list is {numbers_list[-2]}")

# len() tO fInD tHe lEngTh
print(f"The Length of the list is {len(numbers_list)}")

# list iS muTaBlE
numbers_list[6] = 75
numbers_list[-1] = 99
print(numbers_list)

print("==============================")
# mIx tYpE & nEstEd list
data = [10, "Python", 3.1416, False]
print(data)
print(data[2])

students = [
    ["Tyler Durden", 89, 6.1],
    ["John Wick", 85],
    ["Toji Fushiguro", 91, 6.3]
]
print(students)
print(students[2])
print(students[0][2])

print("==============================")
# list sLiCiNg
print(numbers[1:3])
print(numbers[:5:2])
print(f"Reverse of 'number' "
      f"list {numbers[::-1]}")

print("==============================")
# list iS muTaBlE
print(numbers)
num = numbers
modify_index = int(input("Enter the index position to change: "))
modify_value = int(input("Enter the new value: "))
num[modify_index] = modify_value
print(f"This is 'number' variable list {numbers}")
print(f"This is 'num' variable list {num}")
print("In both 'num' & 'number' list value has modified")

print("==============================")
# iNdePeNdEnT cOpY
print(a)
b = a.copy()
modify_index = int(input("Enter the index position to change: "))
modify_value = int(input("Enter the new value: "))
b[modify_index] = modify_value
print(f"This is 'a' variable list {a}")
print(f"This is 'b' variable list {b}")
print("Only in 'b' list value has modified")
