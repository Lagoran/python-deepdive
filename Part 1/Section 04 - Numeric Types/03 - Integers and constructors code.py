print(type(10))

#help(int(10))

print(int("ff",16))


print(hex(255))

a = 0xff

print(int(a))

def from_base10(n, b):
    if b < 2 :
        raise ValueError('b must be >= 2')
    if n < 0 :
        raise ValueError('Number must be >= 0')
    if n == 0 :
        return [0]
    digits = []
    while n > 0:
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits


print(from_base10(25, 16))

def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode the digits")
    # encoding = ''
    # for d in digits:
    #     encoding += digit_map[d]
    # return encoding
    return ''.join([digit_map[d] for d in digits])

print(encode((from_base10(25, 16)), '0123456789ABCDEF'))

def rebase_from_10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 and base >36:
        raise ValueError("Incorrect request!!")
    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits,digit_map)

    if sign == -1:
        encoding = '-' + encoding
    return encoding

b = rebase_from_10(122334,16)
print(b)
print(int(b, base=16))

b = rebase_from_10(-122334,16)
print(b)
print(int(b, base=16))