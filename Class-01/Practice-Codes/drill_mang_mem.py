x = 7
y = x
c = 1000
d = 1000

print(id(x) == id(y))
print(x is y)

print(id(c) == id(d))
print(c is d)

# a = 10
# b = 10
a = int(input("Enter a number: "))
b = int(input("Enter the same number: "))
if a is b:
    print("a is b = True for a is b")
else:
    print("a is b = False for a is b")
if id(a) == id(b):
    print("a and b have same address")
else:
    print("a and b have different address")
