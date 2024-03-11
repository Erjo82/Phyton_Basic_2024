start = int(input())
stop = int(input())
magic_number = int(input())
combination = 0
magic_condition = False

for first_num in range(start, stop + 1):
    for second_num in range(start, stop + 1):
        combination += 1
        if first_num + second_num == magic_number:
            magic_condition = True
            print(f'Combination N:{combination} ({first_num} + {second_num} = {magic_number})')
            break
    if magic_condition:
        break

else:
    print(f'{combination} combinations - neither equals {magic_number}')
