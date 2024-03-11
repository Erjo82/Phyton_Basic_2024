start_num = int(input())
stop_num = int(input())

for number in range(start_num, stop_num + 1):
    num_to_string = str(number)
    odd_sum = 0
    even_sum = 0

    for index, digit in enumerate(num_to_string):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)

    if odd_sum == even_sum:
        print(number, end=' ')

