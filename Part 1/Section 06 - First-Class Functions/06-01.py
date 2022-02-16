help(print)

def func(a,b):
    '''hahah there is some text needed here
    and even some more wrtitten here'''
    print(a,b)

help(func)

def factorial1(n:'a number to be calculated factorial for',
               cache={})->'factorial calculated result':
    '''Calculates n! (factorial function)

    Inputs:
        n: non-negative integer
    Returns:
        the factorial of n
    '''
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('Calculating {0}!'.format(n))
        result = n * factorial1(n-1)
        cache[n] = result
        return result


print(factorial1(5))
print(factorial1(6))

help(factorial1)
print(factorial1.__doc__)

def my_func(a:str='a',b:int=1)->str:
    return a*b

help(my_func)

def apply_func(x,fn):
    return fn(x)

print(apply_func('abc', lambda x: x[1:] * 3))