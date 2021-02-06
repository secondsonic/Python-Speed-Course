#Collection
#List and Tuples

x = [4, True, 'hi'] #list "mutable"
y = 'hi'
x.append("Hello")
x.extend([9, 8, 7])


print(len(x), len(y))
print(x)

print()

x.pop() #7 removed
print(x.pop()) #8 removed
print(x.pop(1)) #True removed
print(x[1]) #hi
x[0] = True #change 4 to True
print(x)

#print(y) if y = x is reference not copy of it y = x[:] is copy
print('\n')

a = (0,0,2,2) #Tuples no append, remove or change "immutable"

print(a[0]) 