print(bool(1))
print(bool(0))
print(bool(-100))

print(int(1).__bool__())
print(bool(1))

a = []
if a is not None and len(a) > 0 :
    print(a[0])

else:
    print("Nothing to see here")

a = [1]
if a:
    print(a[0])

else:
    print("Nothing to see here")