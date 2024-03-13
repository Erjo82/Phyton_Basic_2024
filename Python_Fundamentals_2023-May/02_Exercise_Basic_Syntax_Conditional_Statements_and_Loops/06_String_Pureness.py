number_of_string = int(input())

for current_string in range(number_of_string):
    new_string = input()
    not_pure_string = False

    for character in new_string:
        if character == ',':
            not_pure_string = True
        elif character == '.':
            not_pure_string = True
        elif character == '_':
            not_pure_string = True
    if not_pure_string:
        print(f'{new_string} is not pure!')
    else:
        print(f'{new_string} is pure.')
