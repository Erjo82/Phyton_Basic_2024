lily_yars = int(input())
washing_makina = float(input())
price_1_toy = int(input())

toys_count = 0
lily_money = 0

for birthday in range(1, lily_yars + 1):
    if birthday % 2 == 0:
        money = (birthday * 5) - 1
        lily_money += money
    else:
        toys_count += 1
toys_money = price_1_toy * toys_count
all_money = (lily_money + toys_money)

if all_money >=  washing_makina:
    money_left = all_money - washing_makina
    print(f'Yes! {money_left:.2f}')

else:
    money_needed = washing_makina - all_money
    print(f'No! {money_needed:.2f}')
