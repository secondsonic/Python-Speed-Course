#Dictonaries (Hashtable or a Map)

x = {'key' : 4}
print(x['key'])

x['key2'] = 5
print(x['key2'])

x[2] = 8

x[3] = [2,1,2,5,7]

print(x)
print('key' in x)
print(x.values())

#usually do it like this
print(list(x.values()))
del x['key2']
print(list(x.keys()))

for key, value in x.items():
    print(key,value)

print()

for key in x:
    print(key)

print()

for key in x:
    print(key,x[key])
