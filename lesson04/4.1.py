from sys import argv

hour, rate, bonus = argv[1:]

salary = int(hour)*int(rate)+int(bonus)

print(salary)