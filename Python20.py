#Map and Filter

x = [1,2,3,5,4,88,9,6,8,5,8,5,1,121,341,5]

#mp = map(lambda x: x + 2, x) same
mp = map(lambda i: i + 2, x)
mp0 = map(lambda i: i * 2, x)
print(list(mp))
print(list(mp0))

print()

#Filter
#only return if it is even
fl = filter(lambda i: i % 2 == 0, x)
print(list(fl))

#OR

def func(i):
    #i = i * 3 something random extra
    return i % 2 == 0

fl0 = filter(func, x)
print(list(fl0))