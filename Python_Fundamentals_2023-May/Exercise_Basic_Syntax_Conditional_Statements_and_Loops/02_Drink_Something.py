years = int(input())
drink = ''
if years <= 14:
    drink = 'toddy'
elif years <= 18:
    drink = 'coke'
elif years <= 21:
    drink = 'beer'
else:
    drink = 'whisky'

print(f'drink {drink}')