import random

help(random.random)

print(random.random())

l = [1,2,3,4,5,6,7,8,9]

print(sorted(l, key = lambda x : random.random()))

print(sorted('1qwedvcdcdz', key = lambda x : random.random()))

print(''.join(sorted('1qwedvcdcdz', key = lambda x : random.random())))

print(ord('a'))