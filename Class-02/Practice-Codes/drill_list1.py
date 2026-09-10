numbers = [10, 30, 20, 90, 80, 70]
num = [5, 3, 1, 7, 4, 9, 3, 5, 7, 3]
single_line = "Leonardo DiCaprio is a really good actor"

numbers.insert(4, 77)
numbers.append(66)
# numbers.append([1, 2, 3]) # adD oNe tHiNg
numbers.extend([22, 44, 33])
print(numbers)

numbers.remove(90)
print(f"After remove(90) operation: {numbers}")

# pop(i) meThOd rEmOvE & rEtuRn iTeM
element_six = numbers.pop(5)
print(f"6th element on the number is {element_six}")

num.sort()
print(f"Sort the array 'num' is {num}")

# num.reverse()
num.sort(reverse= True)
print(f"Reverse the array 'num' is {num}")

count_ele_seven = num.count(7)
print(f"'7' occurs in array 'num' is {count_ele_seven} times")

# count() meThOd iS cAsE-sEnSiTivE, sO 'a' aNd 'A' iS dIffErEnT
count_ele_a = single_line.count('a')
# count_ele_a = name.lower().count("a")
print(f"'a' occurs in string variable 'name' is {count_ele_a} times")

index_ele_a = single_line.index("a")
print(f"'a' position in string variable 'name' is in the {index_ele_a}th")

'''
print("==============================")
search_ele = 'o'
count_ele = 0
# Using enumerate keeps track of both the index and the character
for index_ele, i in enumerate(single_line):
    if i == search_ele:
        print(f"'{search_ele}' position in string variable 'name' is in the {index_ele}th")
        count_ele += 1

print(f"'{search_ele}' occurs in string variable 'name' is {count_ele} times")
print("==============================")
'''

names = ["Tyler", "Gojo", "Geto", "Patrick"]
# mEmBeRsHip: in/ not in
print("Tyler" in names)
print("Bruce" in names)
print("Toji" not in names)