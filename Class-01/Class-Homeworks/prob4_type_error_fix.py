age = input("How old are you brother?: ")

# print("Next year you will be", age + 1)

'''
Traceback (most recent call last):
...
TypeError: can only concatenate str (not "int") to str
'''

age = int(age)
print("Next year you will be", age + 1)