def fact(n: "some non-negative integer") -> "n! or 0 if n <0":
    """Calculate the factorial of a non-negative integer n

    If n is negative it return 0"""

    if n < 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return n * fact(n-1)


fact.short_description = "factorial function"
print(fact.short_description)

print(dir(fact))
print(dir(fact.__doc__))
print(dir(fact.__annotations__))

def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    pass
f = my_func

print(my_func.__name__)

print(f.__name__)

print(f.__code__)

print(dir(f.__code__.co_code))


import inspect

print(inspect.ismethod(f))
print(inspect.isfunction(f))


class MyClass:
    def f_instance(self):
        pass

    @classmethod
    def f_class(cls):
        pass

    @staticmethod
    def f_static():
        pass

print(inspect.isfunction(MyClass.f_class), inspect.ismethod(MyClass.f_class))

print(inspect.isroutine(my_func))

print(inspect.isroutine(MyClass.f_instance))

print(inspect.getsource(MyClass))

print(inspect.getmodule(MyClass))

import math

print(inspect.getmodule(math.sin))


# setting up variable
i = 10

#comm 1
#comm 2

def my_func2(a, b=1):
    #comment inside my_func
    pass

print(inspect.getcomments(my_func2))

# TODO: Provide implementation
def my_func4(a: 'a string',
            b: int = 1,
            *args: 'additional positional args',
            kw1: 'first keyword-only arg',
            kw2: 'second keyword-only arg' = 10,
            **kwargs: 'additional keyword-only args') -> str:
    """does something
       or other"""
    pass

print(inspect.signature(my_func))

type(inspect.signature(my_func4))

sig = inspect.signature(my_func4)

for param_name, param in sig.parameters.items():
    print(param_name, param)


def print_info(f: "callable") -> None:
    print(f.__name__)
    print('=' * len(f.__name__), end='\n\n')

    print('{0}\n{1}\n'.format(inspect.getcomments(f),
                              inspect.cleandoc(f.__doc__)))

    print('{0}\n{1}'.format('Inputs', '-' * len('Inputs')))

    sig = inspect.signature(f)
    for param in sig.parameters.values():
        print('Name:', param.name)
        print('Default:', param.default)
        print('Annotation:', param.annotation)
        print('Kind:', param.kind)
        print('--------------------------\n')

    print('{0}\n{1}'.format('\n\nOutput', '-' * len('Output')))
    print(sig.return_annotation)

print_info(my_func4)