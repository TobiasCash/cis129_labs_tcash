# interactive coffee shop simulator 
# with price calculator

# Top of receipt
print('********************')

# Top message, items and item count input
print('My Coffe and Muffin Shop')
coffeenr = int(input('Number of coffees bought?'))
muffinnr = int(input('Number of muffins bought?'))

# Item cost calculator with tax and total amount
totalcoffee = coffeenr * 5.00
totalmuffin = muffinnr * 4.00
tax = 0.06
total = totalcoffee + totalmuffin \
        + ((totalcoffee + totalmuffin) * tax)

# Reciept body with tax calculation for selected items
print('********************')
print('\n')
print('********************')
print('My Coffe and Muffin Shop Receipt')
print(f'{coffeenr} Coffee at $5 each: $ {totalcoffee}')
print(f'{muffinnr} Muffins at $4 each: $ {totalmuffin}')
print(f'6% tax: $ {(totalcoffee + totalmuffin) * tax}')
print('-------')
print(f'Total: $ {total}')

# End of reciept
print('********************')
