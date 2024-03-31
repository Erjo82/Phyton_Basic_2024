all_number = int(input())
numbers_list = []
filtered_list = []
for current_number in range(all_number):
    number = int(input())
    numbers_list.append(number)

command = input()
if command == 'even':
    for searching_even in numbers_list:
        if searching_even % 2 == 0:
            filtered_list.append(searching_even)
elif command == 'odd':
    for searching_odd in numbers_list:
        if searching_odd % 2 == 1:
            filtered_list.append(searching_odd)
elif command == 'negative':
    for searching_negative in numbers_list:
        if searching_negative < 0 :
            filtered_list.append(searching_negative)
elif command == 'positive':
    for searching_positive in numbers_list:
        if searching_positive >= 0 :
            filtered_list.append(searching_positive)
print(filtered_list)