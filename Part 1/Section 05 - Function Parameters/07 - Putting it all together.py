def func(a, b):
    print(a,b)

func(1,2)
func('hello','world')
func(b='world', a='hello')


def func1(a,b='world',c='!'):
    print(a,b,c)

func1('hello')
func1(a='helloooo',b='great world')

def func2(a, b, *args):
    print(a)
    print(b)
    print(args)

func2(1,2,3,4,5,6)
func2(1,2,3,'x','r')

def func3(*,a,b):
    print(a)
    print(b)

func3(a=1,b=2)

def func4(*,a=1,b):
    print(a)
    print(b)

func4(b=2)

def func5(a,b,*,c,d):
    print(a,b,c,d)

func5(1,2,c=3,d=4,)

def func6(a,b=10,*,c=7,d):
    print(a,b,c,d)

func6(1,d=4,)

def func7(a,b=10,*args,c=7,d):
    print(a,b,args,c,d)

func7(1,2,'x','y',d=4,)

def func7(a,b=10,*args,c=7,d,**kwargs):
    print(a,b,args,c,d,kwargs)

func7(1,'x','y',d=4,f=4,r=6,y=7)


print(1,2,3,sep='\t *** \t',end='\t ***')

def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = int(bool(args)) and min(args)
    avg = (hi + lo)/2
    if log_to_console:
        print("High is {0}, Low is {1}, Avg is {2}".format(hi, lo, avg))
    return avg

avg = calc_hi_lo_avg(1,2,3,4,5)
print(avg)

calc_hi_lo_avg(1,2,3,4,5,log_to_console=True)

