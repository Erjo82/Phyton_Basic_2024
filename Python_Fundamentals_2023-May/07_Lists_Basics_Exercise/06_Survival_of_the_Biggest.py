all_numbers_string = input().split()
remove_number = int(input())
all_numbers_int = []
break_count = 0
break_count2 = 0
for current_number in all_numbers_string:
    all_numbers_int.append(int(current_number))
    all_numbers_int.sort()
for removing in all_numbers_int:
    if break_count >= remove_number:
        break
    all_numbers_string.remove(str(removing))
    break_count += 1
for string in all_numbers_string:
    if break_count2 == len(all_numbers_string) - 1:
        print(string)
        break
    else:
        print(string, end=', ')
    break_count2 += 1
