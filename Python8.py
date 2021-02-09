#For Loop

for i in range(10): #1-10  range in order (start, stop, step)
    print(i+1)

print()

for i in range(10,-1,-1): #from 10 to -1 without -1
    print(i)

print()

x = [0,5,4,9,11]
for i in x:
    print(i) 

print()

for i in range(len(x)):
       print(x[i]) #seems like this is the legit way

print()

for i, element in enumerate(x):
    print(i,'->',element)