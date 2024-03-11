flowers_type = input()
pcs_flowers = int(input())
budget = int(input())
discount = 0
price_1_pcs = 0

if flowers_type == 'Roses':
    price_1_pcs = 5
    if pcs_flowers > 80:
        discount = 0.10
elif flowers_type == 'Dahlias':
    price_1_pcs = 3.8
    if pcs_flowers > 90:
        discount = 0.15

elif flowers_type == 'Tulips':
    price_1_pcs = 2.8
    if pcs_flowers > 80:
        discount = 0.15

elif flowers_type == 'Narcissus':
    price_1_pcs = 3
    if pcs_flowers < 120:
        discount = -0.15

elif flowers_type == 'Gladiolus':
    price_1_pcs = 2.5
    if pcs_flowers < 80:
        discount = -0.20

total_sum = pcs_flowers * price_1_pcs * (1 - discount)

if budget >= total_sum:
    money_left = budget - total_sum
    print(f'Hey, you have a great garden with {pcs_flowers} {flowers_type} and {money_left:.2f} leva left.')
else:
    money_needet = total_sum - budget
    print(f'Not enough money, you need {money_needet:.2f} leva more.')
