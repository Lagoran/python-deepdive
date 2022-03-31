l=[5, 8, 6, 10, 9]

print(min(l))
print(max(l))
print(sum(l))
print(any(l))
print(all(l))

from functools import reduce

n = 5
print(reduce(lambda a, b: a * b, range(1, n+1)))

l = []
print(reduce(lambda x, y: x*y, l, 1))