budget = float(input())
flour_price = float(input())
egg_price = flour_price * 0.75
milk_price = flour_price * 1.25
one_loaves_price = egg_price + flour_price + (milk_price * 0.25)
number_of_loaves = int(budget / one_loaves_price)
total_lost_eggs = 0
win_eggs = 0
for current_loaves in range(1, number_of_loaves + 1):
    if current_loaves % 3 == 0:
        total_lost_eggs += (current_loaves - 2)
        win_eggs += 3
    else:
        win_eggs += 3
colored_eggs = win_eggs - total_lost_eggs
money_left = budget - (one_loaves_price * number_of_loaves)
print(f'You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.')
