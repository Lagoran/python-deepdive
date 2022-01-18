import time

def compare_string_using_equals(n):
    string_1 = 'this has to be a long string' * 300
    string_2 = 'this has to be a long string' * 300
    for i in range(n):
        if string_1 == string_2 :
            pass

def compare_string_using_memory_address(n):
    string_1 = 'this has to be a long string' * 300
    string_2 = 'this has to be a long string' * 300
    for i in range(n):
        if string_1 is string_2 :
            pass

start = time.perf_counter()
compare_string_using_equals(10000000)
end = time.perf_counter()
equality1 = end-start
print('equality: ', equality1)

start = time.perf_counter()
compare_string_using_memory_address(10000000)
end = time.perf_counter()
equality2 = end-start
print('equality: ', equality2)
print('difference: ' + str(equality1/equality2) + ' times')
