try:
    m = input('Enter a number month:')

    mounth = {'1':'winter',
        '2':'winter',
        '3':'spring',
        '4':'spring',
        '5':'spring',
        '6':'summer',
        '7':'summer',
        '8':'summer',
        '9':'autumn',
        '10':'autumn',
        '11': 'autumn',
        '12':'winter'}

    print (mounth [m])

except KeyError:
    print('invalid value')
except ValueError:
    print('invalid value')

season = ['winter', 'spring', 'summer','autumn']

if (m == '1') or (m == '2') or (m == '12'):
    print (season[0])
elif (m == '3') or (m == '4') or (m == '5'):
    print(season[1])
elif (m == '6') or (m == '7') or (m == '8'):
    print(season[2])
elif (m == '9') or (m == '10') or (m == '11'):
    print(season[3])
else: print('invalid value')




