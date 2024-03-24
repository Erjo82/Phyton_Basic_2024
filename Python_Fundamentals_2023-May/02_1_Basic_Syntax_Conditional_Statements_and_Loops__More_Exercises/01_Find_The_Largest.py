number = int(input())
number_list = []
for write_list in str(number):
    number_list.append(write_list)
    number_list.sort()
big_number = ''
for current_number in number_list:
    big_number += current_number

print(big_number[::-1])
