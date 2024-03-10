import math

magnolia = int(input())
zuimbul = int(input())
roses = int(input())
cactus = int(input())
gift_price = float(input())

all_flower_price = (magnolia * 3.25 + zuimbul * 4 + roses * 3.5 + cactus * 8)
price_after_taxes = all_flower_price - (all_flower_price * 0.05)

if gift_price > price_after_taxes:
    left_money = math.ceil(gift_price - price_after_taxes)
    print(f'She will have to borrow {left_money} leva.')

else:
    needed_money = math.floor(price_after_taxes - gift_price)
    print(f'She is left with {needed_money} leva.')