budget = float(input())
category = input()
people_pcs = int(input())

ticket_price = 0
money_after_transport = 0

if 1 <= people_pcs <= 4:
    transport = budget * 0.25
    money_after_transport = budget * 0.75     # 75% за транспорт

elif 5 <= people_pcs <= 9:
    money_after_transport = budget * 0.60  # 60% за транспорт

elif 10 <= people_pcs <= 24:
    money_after_transport = budget * 0.50  # 50% за транспорт

elif 25 <= people_pcs <= 49:
    money_after_transport = budget * 0.40  # 40% за транспорт

else:
    money_after_transport = budget * 0.25  # 25% за транспорт

if category == 'Normal':
    ticket_price = 249.99 * people_pcs
else:
    ticket_price = 499.99 * people_pcs

left_budget = budget - money_after_transport - ticket_price

if left_budget > 0:
    left_budget = budget - money_after_transport - ticket_price
    print(f'Yes! You have {left_budget:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(left_budget):.2f} leva.')