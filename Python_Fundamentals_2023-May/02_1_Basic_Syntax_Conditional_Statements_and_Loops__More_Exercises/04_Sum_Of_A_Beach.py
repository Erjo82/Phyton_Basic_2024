word = input().lower()
find_word = 0
for index, sand in enumerate(word): # ------ sand & sun -----------
    if sand == 's':
        find_sand = word[index : index + len('sand')]
        find_sun = word[index: index + len('sun')]
        if find_sand == 'sand':
            find_word += 1
        elif find_sun == 'sun':
            find_word += 1
for index3, water in enumerate(word): # ------ water -----------
    if water == 'w':
        find_water = word[index3 : index3 + len('water')]
        if find_water == 'water':
            find_word += 1
for index4, fish in enumerate(word): # ------ fish -----------
    if fish == 'f':
        find_fish = word[index4 : index4 + len('fish')]
        if find_fish == 'fish':
            find_word += 1
print(find_word)
