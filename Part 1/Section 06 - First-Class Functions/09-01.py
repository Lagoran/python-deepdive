from functools import partial

def my_func(a,b,c):
    print(a,b,c)

f = partial(my_func, 10)

f(20,30)

fn = lambda b,c : my_func(10, b , c)

print(fn(20,30))

def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)

f1 = partial(my_func, 10, k1='a')

f1(20, 30, 40, k2='b', k3='c')

def power(base,exponent):
    return base**exponent

print(power(2,3))

test_power = partial(power,exponent=2)

print(test_power(3))

print(test_power(3, exponent = 5))

origin = (0,0)

l = [(1,1), (0, 2), (-3, 2), (0,0), (10, 10)]

dist2 = lambda x,y: (x[0]-y[0])**2 + (x[1]-y[1])**2

def dist3(x,y):
    return (x[0]-y[0])**2 + (x[1]-y[1])**2

print(dist2((1,1),(4,5)))

print(sorted(l, key = lambda x : dist2((0,0), x)))

print(sorted(l, key = partial(dist2, (0,0))))

print(sorted(l, key = partial(dist3, (0,0))))

import inspect
import json

lines = inspect.getsource(json)
print(lines)