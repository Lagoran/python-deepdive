#map, reduce, filter, list cpmprehensions and generators

help(map)

def fact(n):
    return 1 if n < 2 else n * fact(n-1)

print(fact(5))

map(fact,[1,2,3,4,5,6])

l = list(map(fact,[1,2,3,4,5]))
print(l)

l1 = [1, 2, 3, 4, 5]

l2 = [6, 7, 8, 9, 10]

f = lambda x, y: x*y

t = map(f,l1,l2)

print(list(t))

#Filter

help(filter)
l = [1,2,3,4,5,0]

for e in l :
    print(e)

for t in filter(None,l):
    print(t)

def filter_is_even(n):
    return n if n%2 == 0 else 0

f = filter(filter_is_even,l)

print(f)

print(list(f))

g = filter(lambda x : x%2 == 0, l)

print(type(g))

print(list(g))

print("smthg")

#alternative to map and filter using list comprehensions

#in case we need to produce a list with factorials from a list of digits

l3 = [1,2,3,4,5,66]
u = [fact(i) for i in l3]
print(type(u))
print(u)

z1 = [1,2,3,4,5,6]
z2 = ['a','b','x','d','e','r']
print(list(zip(z1,z2)))

zz = (zip(range(100),z1))

unzipped = zip(*zz)

print(list(unzipped))

zztop = zip((0, 1, 2, 3, 4, 5),(1, 2, 3, 4, 5, 6))

print(type(zztop))
print(list(zztop))

unzipped2 = zip(*zztop)

print(list(zip(*zztop)))

lzz = [1,2,3,4,5,66]
zzz = [1,2,3,4,5,6]

result_z = [i + z for i,z in zip(lzz,zzz)]
print(result_z)


result_f = [i - z for i,z in zip(lzz,zzz) if i > 10]
print(result_f)

gg = filter(lambda y:y < 35,map(lambda x:x ** 2, range(111)))

print(gg)
print(list(gg))

print([x ** 2 for x in range(111) if x ** 2 < 35])