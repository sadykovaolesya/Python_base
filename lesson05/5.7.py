import json

my_list = []
dict_firm_p = {}
dict_firm_l = {}
dict_average_p = {}
with open('my_file_7.txt') as f:
    count = 0
    average_profit = 0
    for line in f:
        content = line.split()
        profit = int(content[2]) - int(content[3])
        print(f'Profit {content[0]} - {profit}')
        if profit > 0:
            dict_firm_p[content[0]] = profit
            average_profit += profit
            count += 1
        else:
            dict_firm_l[content[0]] = profit
average_profit = int(average_profit / count)
dict_average_p['average_profit'] = average_profit
print('Average - ',int(average_profit/count))
my_list = [dict_firm_p,dict_firm_l,dict_average_p]

with open('profit.json', 'w') as f:
    json.dump (my_list,f)





