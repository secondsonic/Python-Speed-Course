#SETS
#sets are much faster the s = [] as the input gets larger
x = set()

s = {4,5,6,9,4,4,5,5,5,5,9} #is a dict
s2 = {5,9,8,7,7,2}
print(type({}))
s.add(1) #or set.add
s.remove(5)
print(s)
print(1 in s)
print(s.union(s2))
print(s.difference(s2))
print(s.intersection(s2))
print(s.issubset(s2))

