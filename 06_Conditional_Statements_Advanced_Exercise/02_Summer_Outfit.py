dagree = int(input())
daytime = input()
outfit = ''
shoes = ''

# 10 <= градуси <= 18
# 18 < градуси <= 24
# градуси >= 25


if 10 <= dagree <= 18:
    if daytime == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif daytime == 'Afternoon':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif daytime == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

if 18 < dagree <= 24:
    if daytime == 'Morning':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif daytime == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif daytime == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

if dagree >= 25:
    if daytime == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif daytime == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    elif daytime == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f'It\'s {dagree} degrees, get your {outfit} and {shoes}.')
