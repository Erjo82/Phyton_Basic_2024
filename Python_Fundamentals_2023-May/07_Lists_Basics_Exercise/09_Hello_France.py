all_items = input().split('|')
budget = float(input())
first_budget = budget
sells_list = []
traint_ticket = 150
profit = 0
available_money = 0

for items in all_items:
    price_is_ok = True
    current_item, items_price_string = items.split('->')
    items_price = float(items_price_string)

    if current_item == 'Clothes':
        if items_price > 50.00:
            price_is_ok = False
    elif current_item == 'Shoes':
        if items_price > 35.00:
            price_is_ok = False
    elif current_item == 'Accessories':
        if items_price > 20.50:
            price_is_ok = False
    if price_is_ok:
        if budget >= items_price:
            budget -= items_price
            cell_price = (items_price * 1.4)
            sells_list.append(f'{cell_price:.2f}')
            profit += cell_price - items_price
            available_money += cell_price

for all_cells in sells_list:
    print(all_cells, end=' ')

print()
print(f'Profit: {profit:.2f}')
if available_money + budget >= traint_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')
