from math import isclose, trunc, floor, ceil



x = 0.1 + 0.1 + 0.1
y = 0.3
print(isclose(x, y))

x = 123456789.01
y = 123456789.02
print(isclose(x, y))


print(isclose(123456789.01, 123456789.02, rel_tol=0.01))
print(isclose(0.01, 0.02, rel_tol=0.01))
x = 0.0000001
y = 0.0000002

print(isclose(x, y, rel_tol=0.01))

x = 0.0000001
y = 0.0000002

a = 123456789.01
b = 123456789.02

print('x = y:', isclose(x, y, abs_tol=0.0001, rel_tol=0.01))
print('a = b:', isclose(a, b, abs_tol=0.0001, rel_tol=0.01))

print(trunc(10.3), trunc(-10.3), floor(10.3), floor(-10.3), ceil(10.4), ceil(-10.3), round(10.56, 0), round(10.56, 1), round(10.56, 2), round(10.56, -1), round(10.56, -2))