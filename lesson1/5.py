proceeds = int (input('Enter proceeds'))
cost = int (input('Enter cost'))

if proceeds > cost:
    print ('Profit')
    profit = proceeds - cost
    staff = int (input('Enter staff'))
    profitable = profit /proceeds *100
    profit_staff = profit /staff
    print(f'Profitability - {profitable:.2f}% ,Employee profit - {profit_staff:.2f}' )

else:
    print('Loss')