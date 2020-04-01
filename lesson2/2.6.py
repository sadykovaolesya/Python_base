goods = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
         (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
         (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})]


about_goods = {}

for el in goods:

        for key, value in el[1].items():
            if key in about_goods:
                try:
                    about_goods[key].append(value)
                except AttributeError:
                    about_goods[key] = [about_goods[key] , value]
            else:
                   about_goods[key] = value


print(about_goods)

