kilometre = int(input())
day_or_night = input()

if kilometre < 20:
    if day_or_night == 'day':
        all_kilometres = 0.7 + (0.79 * kilometre)
    else:
        all_kilometres = 0.7 + (0.90 * kilometre)

elif kilometre < 100:
    all_kilometres = 0.09 * kilometre

else:
    all_kilometres = 0.06 * kilometre

print(f'{all_kilometres:.2f}')
