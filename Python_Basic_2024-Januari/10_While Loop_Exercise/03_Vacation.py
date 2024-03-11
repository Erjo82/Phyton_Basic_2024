excursion_money = float(input())
available_money = float(input())
days_counter = 0
spending_counter = 0

while available_money < excursion_money and spending_counter < 5:
    spend_or_save = input()
    money = float(input())
    days_counter += 1

    if spend_or_save == 'spend':
        available_money -= money
        spending_counter += 1
        if available_money < 0:
            available_money = 0

    elif spend_or_save == 'save':
        available_money += money
        spending_counter = 0

if spending_counter == 5:
    print(f'You can\'t save the money.')
    print(days_counter)

if available_money >= excursion_money:
    print(f'You saved the money for {days_counter} days.')


