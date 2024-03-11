# Да се напише програма, която чете две цели числа
# въведени от потребителя и отпечатва по-голямото от двете.

num_1 = int(input())
num_2 = int(input())
big_num = 0

if num_1 > num_2:
    big_num = num_1
else:
    big_num = num_2
print(big_num)

