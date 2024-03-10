days = int(input()) - 1
room_type = input()
rating = input()
days_price = 0

if room_type == 'room for one person':
    days_price = days * 18

elif room_type == 'apartment':
    days_price = days * 25
    if days < 10:
        days_price = days_price * (1 - 0.30)
    elif days <= 15:
        days_price = days_price * (1 - 0.35)
    else:
        days_price = days_price * (1 - 0.50)

elif room_type == 'president apartment':
    days_price = days * 35
    if days < 10:
        days_price = days_price * (1 - 0.10)
    elif days <= 15:
        days_price = days_price * (1 - 0.15)
    else:
        days_price = days_price * (1 - 0.20)

if rating == 'positive':
    days_price = days_price * (1 + 0.25)

else:
    days_price = days_price * (1 - 0.10)
print(f'{days_price:.2f}')
