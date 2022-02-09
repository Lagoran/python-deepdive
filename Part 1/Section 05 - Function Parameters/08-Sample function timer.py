import time

def time_it(fn, *args, rep=5, **kwargs):
    start= time.perf_counter()
    for i in range(rep):
        fn(*args,**kwargs)
    end = time.perf_counter()
    return (end - start) / rep

time_it(print, 1, 2, 3,sep='-')

time_it(print, 1, 2, 3, sep='-', end=' *** ', rep=3)

def compute_powers_1(n, *, start = 1, end):
    #using a for loop
    result = []
    for i in range(start,end):
        result.append(n**i)
    return result

def compute_powers_2(n, *, start = 1, end):
    #using list comprehension
    return [n**i for i in range(start,end)]

def compute_powers_3_gen(n, *, start = 1, end):
    #using generator
    return (n ** i for i in range(start, end))

def compute_powers_3(n, *, start = 1, end):
    #using generator
    return list((n ** i for i in range(start, end)))

print(compute_powers_1(2,end=6))

print(time_it(compute_powers_1,100,end = 100,rep = 1000))
print(time_it(compute_powers_2,100,end = 100,rep = 1000))
print(time_it(compute_powers_3_gen,100,end = 100,rep = 1000))
print(time_it(compute_powers_3,100,end = 100,rep = 1000))

print(compute_powers_3(2,end = 100))