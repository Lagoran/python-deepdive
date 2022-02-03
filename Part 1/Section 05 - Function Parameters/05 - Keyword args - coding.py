def func1(a, b, c):
    print(a, b, c)

print(func1(1,2,3))

print(func1(a=1,b=2,c=3))

def func2(a, b, c, *args, d):
   print(a, b, c, args, d)

print(func2(1,2,3,4,5,d=6))


def func3(*args, d):
   print(args, d)

print(func3(1,2,3,4,5,d=8))

def func3(*args, d):
   print(args, d)

print(func3(1,2,3,4,5,d='hello'))

print(func3(d='hello'))

def func4(*args, d=2):
   print(args, d)

print(func4(1,2,3,4,5))

def func6(*, d='hello'):
    print(d)


print(func6(d='gg izi'))

def func7(a, *, b='hello', c):
    print(a, b, c)

print(func7(1, c='ehooo', b='hohoho'))

def func11(a, b=20, *args, d=0, e='n/a'):
    print(a, b, args, d, e)

print(func11(5, 4, 3, 2, 1, d=0, e='all engines running'))

func11(0, 600, d='goooood morning', e='python!')

func11(11, 'm/s', 24, 'mph', d='unladen', e='swallow')

