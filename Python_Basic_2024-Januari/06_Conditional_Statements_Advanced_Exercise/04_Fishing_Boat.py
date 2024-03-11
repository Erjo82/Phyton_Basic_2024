budget = int(input())
season = input()  # "Spring", "Summer", "Autumn" или "Winter";
fisherman_pcs = int(input())

boat_rent = 0
if season == 'Spring':
    boat_rent = 3000

elif season == 'Summer' or season == 'Autumn':
    boat_rent = 4200

elif season == 'Winter':
    boat_rent = 2600

discount = 0
if fisherman_pcs <= 6:
    discount = 0.10
elif fisherman_pcs <= 11:
    discount = 0.15
elif fisherman_pcs >= 12:
    discount = 0.25

extra_discount = 0
if fisherman_pcs % 2 == 0 and season != 'Autumn':
    extra_discount = 0.05

total_sum = boat_rent * (1 - discount) * (1 - extra_discount)

if budget >= total_sum:
    money_left = budget - total_sum
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_needed = total_sum - budget
    print(f'Not enough money! You need {money_needed:.2f} leva.')
