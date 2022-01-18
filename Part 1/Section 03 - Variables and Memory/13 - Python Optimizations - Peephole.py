def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 10
    f = [1, 2] * 5

print(my_func.__code__.co_consts)


def my_func():
    if e in {1, 2, 3}:
        pass

print(my_func.__code__.co_consts)


import string
import time

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

print(char_list)
print()
print(char_tuple)
print()
print(char_set)

def membership_test(n, container):
    for i in range(n) :
        if 'p' in container :
            pass

start = time.perf_counter()
membership_test(10000000,char_list)
end = time.perf_counter()
equality1 = end-start
print('char equality: ', equality1)

start = time.perf_counter()
membership_test(10000000,char_tuple)
end = time.perf_counter()
equality1 = end-start
print('tuple equality: ', equality1)

start = time.perf_counter()
membership_test(10000000,char_set)
end = time.perf_counter()
equality1 = end-start
print('set equality: ', equality1)