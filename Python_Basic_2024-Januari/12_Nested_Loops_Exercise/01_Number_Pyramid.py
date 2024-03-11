num = int(input())
pyramid_number = 1
is_current_bigger_from_n = False

for row in range(1, num + 1):
    for column in range(1, row + 1):

        if pyramid_number > num:
            is_current_bigger_from_n = True
            break

        print(f'{pyramid_number} ', end="")
        pyramid_number += 1

    if is_current_bigger_from_n:
        break

    print()
