from math import floor, ceil

x = int(input())
y = float(input())
needed_wine = int(input())
workers = int(input())

all_grapes = x * y
wine = (all_grapes * 0.4) / 2.5

if wine >= needed_wine:
    left_wine = wine - needed_wine
    wine_per_worker = left_wine / workers
    print(f'Good harvest this year! Total wine: {floor(wine)} liters.')
    print(f'{ceil(left_wine)} liters left -> {ceil(wine_per_worker)} liters per person.')

else:
    lacking_wine = needed_wine - wine
    print(f'It will be a tough winter! More {floor(lacking_wine)} liters wine needed.')

