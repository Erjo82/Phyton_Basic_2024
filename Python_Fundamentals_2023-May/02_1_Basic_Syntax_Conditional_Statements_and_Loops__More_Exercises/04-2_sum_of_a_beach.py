word = input().lower()
searching_word_list = ['sand', 'sun', 'water', 'fish']
found_word = 0
for current_word in searching_word_list:
    found_word += word.count(current_word)
print(found_word)

