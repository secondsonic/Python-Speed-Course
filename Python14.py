#Functions

#funtions are objects

def func( x , y):
    print('Run', x, y)
    def func():
        print('RUN!')
    func()    

func('You', 'Piece of Shit')

print()

def func(x , y):
    print('Hello')
    return x + y, x * y, x - y, int(x / y)
print(func(4,3))     

print()
print(func(4,3)[0]), print(func(4,3)[1])

#Cleaner and faster way
print()
r1, r2, r3, r4 = func(4,3)
print(r1,r2,r3,r4)

#3 parameters
print()
def func(x, y, z=None):
    print('Run', x, y, z)
    return y * x, int(y / x)
r1, r2 = func(1, 2, 3)
r3, r4 = func(2,3)
print(r1, r2)
print(r3, r4)

