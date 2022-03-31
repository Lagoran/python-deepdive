import operator

print(dir(operator))

print(operator.add(1,3),operator.mul(1,3),
      operator.pow(1,3))

from functools import reduce

print(reduce(lambda x, y: x*y, [1,2,3,4,5]))

print(reduce(operator.mul, [1,1,2,3,4,5]))

print(operator.lt(1,3))
print(operator.lt(1,1))
print(operator.le(1,1))
print(operator.truth(1))


my_list = [1,2,3,4,5]
print(my_list[1])
my_list[1] = 1000
del my_list[2]
print(my_list)

f = operator.itemgetter(2)

print(f(my_list))

x = 'python'

print(f(x))


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('test method running...')


obj = MyClass()

print(obj.a, obj.b, obj.c)

g = operator.attrgetter('a')

print(g(obj))

my_var = 'b'
print(operator.attrgetter(my_var)(obj))

s = operator.attrgetter('a','b','c')

print(s(obj))

z = operator.attrgetter('test')

t = z(obj)

t()

print(operator.itemgetter(2,3)('python123'))

l = [10+1j, 8+2j, 5+3j]
print(sorted(l, key=operator.attrgetter('real')))

test_list = ['aaa','bbb','ede']
print(sorted(test_list, key=operator.itemgetter(-1))

test_dir_tup = [(2, 3, 4), (1, 2, 3), (4, ), (3, 4)]
print(sorted(test_dir_tup, key=operator.itemgetter(0))