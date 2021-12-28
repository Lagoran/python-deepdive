def process(s):
    print('initial s # = {0}'.format(hex(id(s))))
    s = s + ' world'
    print('s after change # = {0}'.format(hex(id(s))))

my_var = 'hello_world'

print(hex(id(my_var)))

print('my_var # = {0}'.format(id(my_var)))
print('my_var # = {0}'.format(hex(id(my_var))))

process(my_var)



def modify_list(lst):
    print('initial lst # = {0}'.format(hex(id(lst))))
    lst.append(100)
    print('Final lst # = {0}'.format(hex(id(lst))))

my_list = [1,2,3]
print(hex(id(my_list)))

modify_list(my_list)

print(my_list)

