from decimal import Decimal, getcontext
getcontext().prec = 10
unit_price = Decimal(2.32).quantize(Decimal('0.00'))
price2 = '{0:.2f}'.format(unit_price)
print(price2)
number_sold = 3
money_received = Decimal(6.96).quantize(Decimal('0.00'))
print(money_received)
if unit_price * number_sold == money_received:
    print('Accounts balanced')
else:
    raise ValueError('Accounts not balanced')


TWOPLACES = Decimal(10) ** -2       # same as Decimal('0.01')
THREEPLACES = Decimal(10) ** -3
FOURPLACES = Decimal(10) ** -4
print(TWOPLACES)
two_place = Decimal(3.214).quantize(TWOPLACES)
three_place = Decimal(3.214).quantize(THREEPLACES)
four_place = Decimal(3.214).quantize(FOURPLACES)
print(two_place)
print(three_place)
print(four_place)