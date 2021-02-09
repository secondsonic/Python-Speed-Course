#Slice Operator
#works on Tuples and Strings too
x = [0,1,2,3,4,5,6,7,8,9]
y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = "Hello"

#sliced = [start:stop:step]
sliced0 = x[0:5:2]
print(sliced0)

sliced1 = x[2:]
print(sliced1)

sliced2 = x[:4]
print(sliced2)

sliced3 = x[5:1:-1]
print(sliced3)

xInverse = x[::-1]
print(xInverse)