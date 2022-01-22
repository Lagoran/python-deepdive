import decimal
from decimal import Decimal

g_ctx = decimal.getcontext()
print(g_ctx.prec, g_ctx.rounding)

x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1))
print(round(y, 1))

g_ctx.prec = 6
g_ctx.rounding = decimal.ROUND_HALF_UP

print(g_ctx.prec, g_ctx.rounding)

print(decimal.getcontext().prec)

x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1))
print(round(y, 1))

# with decimal.localcontext() as ctx:
#     print(ctx.prec)
#     print(ctx.rounding)
#
# with decimal.localcontext() as ctx:
#     ctx.prec = 10
#     print('local prec = {0}, global prec = {1}'.format(ctx.prec, g_ctx.prec))
#
#     print(decimal.getcontext().rounding)
#     x = Decimal('1.25')
#     y = Decimal('1.35')
#     print(round(x, 1))
#     print(round(y, 1))
#
#     decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
#     print(decimal.getcontext().rounding)
#
#     x = Decimal('1.25')
#     y = Decimal('1.35')
#     print(round(x, 1))
#     print(round(y, 1))

decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN

x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1), round(y, 1))
with decimal.localcontext() as ctx:
    ctx.rounding = decimal.ROUND_HALF_UP
    print(round(x, 1), round(y, 1))
print(round(x, 1), round(y, 1))


decimal.getcontext().prec = 6

a = Decimal('0.12345')
b = Decimal('0.12345')
c = a + b
print(c)

with decimal.localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print(c)

print(c)


print(format(0.1, '.25f'))

print(Decimal(0.1))