budget = int(input())
bought_everything = False

while budget >= 0:
    command = input()
    if command == 'End':
        bought_everything = True
        break
    current_buy = int(command)
    budget -= current_buy

if bought_everything:
    print('You bought everything needed.')
else:
    print('You went in overdraft!')