#Comprehensions

x = [x + 1 for x in range(5)]
y = [y % 5 for y in range(5)]
z = [0 for z in range(5)]

a = [[0 for a in range(5)] for a in range(5)]

b = [i for i in range(100) if i % 5 == 0]

#for dictonaries
c = {c:0 for c in range (100) if c % 10 == 0}

#for set
d = {i for i in range (100) if i % 10 == 0}
e = set(i for i in range (100) if i % 10 == 0)

#for tuple

f = tuple(i for i in range(100) if i % 5 == 0)

print(x)
print(y)
print(z)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)





