from fractions import Fraction

help(Fraction)

a= Fraction(numerator=3,denominator=9) + Fraction('22/7')

print(a)
print(Fraction(numerator=3,denominator=9))

print(Fraction('22/7'))
print(a.limit_denominator(1))

print(format(0.1, '.250f'))

c = 0.1 + 0.1 + 0.1
d = 0.3

print(c == d)