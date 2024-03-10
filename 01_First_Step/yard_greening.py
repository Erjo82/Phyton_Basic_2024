total_yard = float(input())
price_yard = total_yard * 7.61
discount = price_yard * 0.18
discount_price = price_yard - discount

print (f"The final price is: {discount_price} lv.")
print (f"The discount is: {discount} lv.")