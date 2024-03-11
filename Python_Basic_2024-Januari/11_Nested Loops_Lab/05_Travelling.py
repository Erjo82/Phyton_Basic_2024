while True:
    spending_money = 0
    destination = input()
    if destination == 'End':
        break
    needed_money = float(input())

    while spending_money < needed_money:
        money = float(input())
        spending_money += money
        if spending_money >= needed_money:
            print(f'Going to {destination}!')
