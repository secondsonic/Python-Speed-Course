#Unpack Operator, *ARGS and **KWARGS

#fucntions are objects
def func(x):
    def func2():
        print(x)

    return func2

print(func(3))
print(func(3)())
func(3)()
x = func(3)
x()

print

def func(*args, **kwargs):
    pass

#unpack operator *x
#kwargs stands for key arguments
x = [1, 5, 9, 8, 10 ,-5 ,0]
print(x)
print(*x)

print

def func(x, y):
    print(x, y)
    print(x + y)
    print()

pairs = [(1,2), (3,4), (5,6)]

for pair in pairs: #works but not the pythonic way!
    func(pair[0], pair[1])

for pair in pairs:
    func(*pair)
print

#now for dictonaries
#if we have keys
for pair in pairs:
    func(**{'x':2, 'y':5 })

#Also this way

def func(x, y):
    print(x, y)

func(**{'x':3, 'y':9 })
#works even when not in right order
func(**{'y':9, 'x':3 })

print

def func(*args, **kwargs):
    print(*args, **kwargs)
#if just (one=0, two=1) Erroe:'one' is an invalid keyword argument for print()
func(1,2,3,4,5, {'one':0, 'two':1})
