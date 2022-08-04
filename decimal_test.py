from decimal import Decimal, getcontext
getcontext().prec = 10
unit_price = Decimal(2.32).quantize(Decimal('0.00'))
print(unit_price)
number_sold = 3
money_received = Decimal(6.96).quantize(Decimal('0.00'))
print(money_received)
if unit_price * number_sold == money_received:
    print('Accounts balanced')
else:
    raise ValueError('Accounts not balanced')