import decimal
from decimal import Decimal

import math

x = 10
y = 3

print(x//y, x%y)
print(divmod(x,y))

print(type(x))
print(math.sqrt(x))

print(x == y*(x//y)+(x%y))

x = Decimal(-10)
y = Decimal(3)

print(x//y, x%y)
print(divmod(x,y))

print(x == y*(x//y)+(x%y))

import sys


a = 3.1415
b = Decimal('3.1415')

print(sys.getsizeof(a))
print(sys.getsizeof(b))

import time
from decimal import Decimal


def run_float(n=1):
    for i in range(n):
        a = 3.1415


def run_decimal(n=1):
    for i in range(n):
        a = Decimal('3.1415')


n = 10000000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end-start)


def run_float(n=1):
    a = 3.1415
    for i in range(n):
        a * a


def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a * a


start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end - start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end - start)

n = 5000000

import math


def run_float(n=1):
    a = 3.1415
    for i in range(n):
        math.sqrt(a)


def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a.sqrt()


start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end - start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end - start)


