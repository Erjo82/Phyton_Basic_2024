word = input().lower()
find_word = 0
is_water = 'water'
is_sand = 'sand'
is_sun = 'sun'
is_fish = 'fish'

for index, sand in enumerate(word): # ------ sand -----------
    if sand == 's':
        find_sand = word[index : index + len(is_sand)]
        if find_sand == is_sand:
            find_word += 1
for index2, sun in enumerate(word): # ------ sun -----------
    if sun == 's':
        find_sun = word[index2 : index2 + len(is_sun)]
        if find_sun == is_sun:
            find_word += 1
for index3, water in enumerate(word): # ------ water -----------
    if water == 'w':
        find_water = word[index3 : index3 + len(is_water)]
        if find_water == is_water:
            find_word += 1
for index4, fish in enumerate(word): # ------ fish -----------
    if fish == 'f':
        find_fish = word[index4 : index4 + len(is_fish)]
        if find_fish == is_fish:
            find_word += 1

print(find_word)
