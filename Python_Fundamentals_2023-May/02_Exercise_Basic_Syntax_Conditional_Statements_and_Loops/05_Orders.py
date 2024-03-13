numbers_of_orders = int(input())
total_cost = 0
for current_order in range(numbers_of_orders):
    price_for_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    current_order_price = (price_for_capsule * capsules_needed_per_day) * days
    if price_for_capsule < 0.01 or price_for_capsule > 100:
        continue
    elif days <1 or days> 31:
        continue
    elif capsules_needed_per_day < 1 or capsules_needed_per_day> 2000:
        continue
    print(f'The price for the coffee is: ${current_order_price:.2f}')
    total_cost += current_order_price

print(f'Total: ${total_cost:.2f}')

