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

def func(**kwargs):
    print(kwargs)

func(a=2,b=4)

def func111(*args, **kwargs):
    print(args)
    print(kwargs)

func111(4,5,a=2,b=4)

def func112(*,d,**kwargs):
    print(d)
    print(kwargs)

func112(d=4,f=45,t=56)

# concatenate.py
def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))


# sum_integers_args_3.py
def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2, *list3))

# extract_list_body.py
my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print(a)
print(b)
print(c)

# merging_lists.py
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)

my1dict={"a": 1,"b": 7}
my2dict={"c": 3,"d": 4}
my_mergerdict = {**my1dict,**my2dict}

print(my_mergerdict)

# merging_dicts.py
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)

print(help(print()))