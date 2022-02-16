func = lambda x: x**2

print(type(func))

print(func(3))
func1 = lambda x,y=10 :(x,y)
print(func1(1))

func2 = lambda x, *args, y, **kwargs: (x, args, y, kwargs)
print(func2(1,2,3,4,y=9,u=99))

def func3(x, fn):
    return fn(x)

print(func3(3, lambda x : x**3))

def func4(fn, *args, **kwargs):
    return fn(*args,**kwargs)

print(func4(lambda x, y, z=6: x + y +z, 3, 4))

func6 = lambda x,y : x*y
print(func6('e',7))

l = ['a', 'B', 'c', 'D']

print(sorted(l))

print(sorted(l, key = str.upper))

d = {'def': 300, 'abc': 200, 'ghi': 100}

print(sorted(d))

print(sorted(d, key = lambda k:d[k]))

l1 = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']

print(sorted(l1, key = lambda k : k[-1], reverse=True))

print(sorted(l1, key = lambda k : k[-1]))

help(sorted)

