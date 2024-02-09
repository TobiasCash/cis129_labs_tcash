# interactive coffee shop simulator 
# with price calculator
# available items: coffee, muffins, milkshakes, sandwiches.

# Top of receipt
print('********************')

# Top message, items and item input
print('My Coffe and Muffin Shop')
coffeenr = int(input('Number of coffees bought?'))
muffinnr = int(input('Number of muffins bought?'))
milkshakenr = int(input('Number of milkshakes bought?'))
sandwichnr = int(input('Number of sandwiches bought?'))
name = input('Name for the order?')

# Item cost calculator with tax and total amount
totalcoffee = coffeenr * 5.00
totalmuffin = muffinnr * 4.00
totalmilksh = milkshakenr * 6.00
totalsandw = sandwichnr * 9.00
tax = 0.06
total = totalcoffee + totalmuffin + totalmilksh \
        + totalsandw + ((totalcoffee + totalmuffin \
        + totalmilksh + totalsandw) * tax)

# Reciept body with tax calculation for selected items
print('********************')
print('\n')
print('********************')
print('My Coffe and Muffin Shop Receipt')
print(f'{coffeenr} Coffee at $5 each: $ {totalcoffee}')
print(f'{muffinnr} Muffins at $4 each: $ {totalmuffin}')
print(f'{milkshakenr} Milkshakes at $6.00  each: $ {totalmilksh}')
print(f'{sandwichnr} Sandwich at $9.00 each: $ {totalsandw}')
print(f'6% tax: $ {(totalcoffee + totalmuffin + totalmilksh + totalsandw) * tax}')
print('-------')
print(f'Total: $ {total}')

# End of reciept
print('********************')
print('\n')
print(f'Thank You, {name}! Have a nice day!')
