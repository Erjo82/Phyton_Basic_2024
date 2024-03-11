days = int(input())
hours = int(input())
total_cost = 0

for days_calculation in range(1, days + 1):
    day_cost = 0
    for hours_calculation in range(1, hours + 1):

        price_for_hour = 1
        if days_calculation % 2 == 0 and hours_calculation % 2 != 0:
            price_for_hour += 1.50
        elif days_calculation % 2 != 0 and hours_calculation % 2 == 0:
            price_for_hour += 0.25

        day_cost += price_for_hour
        total_cost += price_for_hour

    print(f'Day: {days_calculation} - {day_cost:.2f} leva')
print(f'Total: {total_cost:.2f} leva')
