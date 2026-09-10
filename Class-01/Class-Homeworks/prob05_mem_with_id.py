a = 200
b = 200
print(a is b)

c = 2000
d = 2000
print(c is d)

# Explanation: In 'a' and 'b' values are from -5 to 256 ,and it saves to cache. So they are
# pointing to the same object. But in 'c' and 'd' values are above 256. So they are pointing
# to the different object. So, in the first situation it prints 'True' but in second situation
# it prints 'False'.
# NB: In Terminal, they work differently one for True one for 'False' but in IDE, they work
# same both is 'True' here.