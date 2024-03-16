first_word = input()
second_word = input()
last_transformation = first_word

for transformation in range(len(first_word)):
    left_side = second_word[:transformation + 1]
    right_side = first_word[transformation + 1 :]
    new_word = left_side + right_side
    if last_transformation == new_word:
        continue
    last_transformation = new_word
    print(new_word)
