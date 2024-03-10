peter_budget = float(input())
video_card_pcs = int(input())
cpu_pcs = int(input())
ram_pcs = int(input())

video_card_price = 250
cpu_price = video_card_price * video_card_pcs * 0.35
ram_price = video_card_price * video_card_pcs * 0.10
all_parts_sum = video_card_price * video_card_pcs + cpu_price * cpu_pcs + ram_price * ram_pcs

if video_card_pcs > cpu_pcs:
    all_parts_sum = all_parts_sum * (1 - 0.15)

money_left = peter_budget - all_parts_sum
money_needed = (all_parts_sum - peter_budget)

if peter_budget >= all_parts_sum:
    print(f'You have {money_left:.2f} leva left!')
else:
    print(f'Not enough money! You need {abs(money_needed):.2f} leva more!')