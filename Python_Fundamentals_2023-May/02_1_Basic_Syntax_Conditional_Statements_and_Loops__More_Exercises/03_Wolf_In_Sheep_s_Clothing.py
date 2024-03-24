list_of_animal = []
animal = input()
word = ''
is_head = False
is_queue = False
wolf = 0

for current_letter in animal:
    if current_letter == ',':
        continue
    elif current_letter == ' ':
        list_of_animal.append(word)
        word = ''
        continue
    word += current_letter
list_of_animal.append(word)
reversed_list = list_of_animal[::-1]

for index,current_animal in enumerate(reversed_list):
    if index == 0 and current_animal == 'wolf':
        is_queue = True
    elif current_animal == 'wolf':
        is_head = True
        wolf = index

if is_queue:
    print(f'Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {wolf}! You are about to be eaten by a wolf!')


