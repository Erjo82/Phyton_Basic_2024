qty_decoration = int(input())
day_to_christmas = int(input())
christmas_spirit = 0
money_spend = 0

for current_day in range(1, day_to_christmas + 1):
    if current_day % 11 == 0:
        qty_decoration += 2
    if current_day % 2 == 0:
        money_spend += 2 * qty_decoration
        christmas_spirit += 5
    if current_day % 3 == 0:
        money_spend += 8 * qty_decoration
        christmas_spirit += 13
    if current_day % 5 == 0:
        money_spend += 15 * qty_decoration
        christmas_spirit += 17
        if current_day % 3 == 0:
            christmas_spirit += 30
    if current_day % 10 == 0:
        christmas_spirit -= 20
        money_spend += 5 + 3 + 15
if day_to_christmas % 10 == 0:
    christmas_spirit -= 30

print(f'Total cost: {money_spend}')
print(f'Total spirit: {christmas_spirit}')




