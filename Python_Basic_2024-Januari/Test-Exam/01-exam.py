sea_price = 680
sea_count = 0
mountain_price = 499
mountain_count = 0
profit = 0


sea_pcs = int(input())
mountain_pcs = int(input())

while True:
    packages_name = input()
     if packages_name == 'Stop':
        break

     elif packages_name == 'sea':
        sea_count += 1
        if sea_count >= sea_pcs:
           sea_price = 0
            profit += sea_price

     elif packages_name == 'mountain':
         mountain_count += 1
         if mountain_count >= mountain_pcs:
                mountain_price = 0
            profit += mountain_price

if sea_count == 0 and mountain_count == 0:
    print(f'Good job! Everything is sold.')

print(f'Profit: {profit} leva.')