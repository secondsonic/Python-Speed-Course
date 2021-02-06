#Scope and Global

#X is global
x = 'Arsalan'

#x is local in the scope of func change cannot be happend from outside
def func(name):
    x = name
print(x)

func('changed')
print(x)

print()

#expected behavior can occur here 
#Naver use it you reference the global scope very very very rare to use it
def func(name):
    global x
    x = name
print(x)

func('changed')
print(x)
