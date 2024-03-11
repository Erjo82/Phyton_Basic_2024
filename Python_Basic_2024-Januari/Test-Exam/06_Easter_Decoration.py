client_pcs = int(input())
average_sum = 0
print()

for all_sells in range(1, client_pcs + 1):
    client_sum = 0
    item_count = 0
    while True:

        product_type = input()
        if product_type == 'Finish':
            if item_count % 2 == 0:
                client_sum = client_sum - (client_sum * 0.2)
            break

        elif product_type == 'basket':
            item_count += 1
            client_sum += 1.50

        elif product_type == 'wreath':
            item_count += 1
            client_sum += 3.80

        elif product_type == 'chocolate bunny':
            item_count += 1
            client_sum += 7

    average_sum += client_sum
    print(f'You purchased {item_count} items for {client_sum:.2f} leva.')

average_sum = average_sum / all_sells
print(f'Average bill per client is: {average_sum:.2f} leva.')
