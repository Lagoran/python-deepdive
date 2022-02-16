from datetime import datetime

def log(msg, *, dt = None):
    dt = dt or datetime.utcnow()
    print("{0} - {1}".format(msg,dt))

log('test')
log('test', dt = '2022-1-1 12:15:59.0000000')

def factorial(n):
    if (n < 1):
        return 1
    else:
        print("Calculating {0}!".format(n))
        return n * factorial(n-1)



def factorial1(n,cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('Calculating {0}!'.format(n))
        result = n * factorial(n-1)
        cache[n] = result
        return result


print(factorial1(5))
print(factorial1(6))
