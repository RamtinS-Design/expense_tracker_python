file = open('expenses.txt', 'w')
file.write('utility,20\n')
file.write('groceries,15\n')
file.write('utility,10\n')
file.write('transportation,25\n')
file.write('outdoors, 12\n')
file.close()

totals = {}

file = open('expenses.txt', 'r')
for line in file:
    category, amount = line.strip().split(',')
    amount = float(amount)

    if category in totals:
        totals[category] += amount
    else:
        totals[category] = amount

file.close()

for category in totals:
    print(category, ':', totals[category])
