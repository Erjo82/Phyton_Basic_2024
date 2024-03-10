trip_cost = float(input())
puzzles_pcs = int(input())
talking_doll_pcs = int(input())
teddy_bear_pcs = int(input())
minions_pcs = int(input())
truck_pcs = int(input())


all_toys_pcs = puzzles_pcs + talking_doll_pcs + teddy_bear_pcs + minions_pcs + truck_pcs
all_toys_money = puzzles_pcs * 2.6 \
                 + talking_doll_pcs * 3 \
                 + teddy_bear_pcs * 4.1 \
                 + minions_pcs * 8.2 \
                 + truck_pcs * 2
discount = 0
if all_toys_pcs >= 50:
    discount = 0.25

price_after_discount = all_toys_money * (1 - discount)  # цена след отстъпка ot 25%
money_after_rent = price_after_discount * (1 - 0.10)  # цена след 10% за наем

if money_after_rent >= trip_cost:
    money_left = money_after_rent - trip_cost
    print(f'Yes! {money_left :.2f} lv left.')
else:
    money_needed = trip_cost - money_after_rent
    print(f'Not enough money! {money_needed :.2f} lv needed.')
