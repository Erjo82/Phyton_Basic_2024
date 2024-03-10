n_num = int(input())

for special_num in range(1111, 10_000):
    special_num_str = str(special_num)

    is_special = True
    for index, ch in enumerate(special_num_str):
        ch_int = int(ch)
        if ch_int == 0:
            is_special = False
            break
        elif n_num % ch_int != 0:
            is_special = False
            break

    if is_special:
        print(special_num, end=' ')

