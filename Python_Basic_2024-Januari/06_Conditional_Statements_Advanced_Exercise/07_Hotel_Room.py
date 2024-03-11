month = input()
days = int(input())
apartment = 0
studio = 0
studio_discount = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if days > 14:
        studio_discount = 0.30
    elif days > 7:
        studio_discount = 0.05

elif month == 'June' or month == 'September':
    studio = 75.20
    apartment = 68.70
    if days > 14:
        studio_discount = 0.20

elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77

if days > 14:
    discount_apartment = 0.10
    apartment_price = (apartment * days) - ((apartment * days) * 0.10)
else:
    apartment_price = (apartment * days)

studio_price = (studio * days) - ((studio * days) * studio_discount)
print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')
