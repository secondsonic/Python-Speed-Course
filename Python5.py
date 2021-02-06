#Conditional Operators

x = "hello"
y = 3
z = 'yes'
print(x + z)
print(x * y)

n = 'hello'

print(x == n)
print(x != n)

#ascii ordinal value
print(ord('a'))
print(ord('Z'))

print("a" > 'Z')

print(7.0 == 7)

result = 5 == 5

print(result)

#Chained conditional
print()
a = 7
b = 8
c = 0

m1 = a == b
m2 = b > a
m3 = c < a + 2
#or can be (a + 2)

#or and not

m4 = m1 or m2
print(m4)

m5 = m1 or m2 or m3
print(m5)

m6 = m1 or not m2 or m3
print(m6)

l = True
k = False

print(not (k and l))
#order not and or
