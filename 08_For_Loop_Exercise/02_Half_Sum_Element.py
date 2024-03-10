import sys

number = int(input())
total_sum = 0
max_number = -sys.maxsize

for nums in range(number):
    num = int(input())
    if num > max_number:
        max_number = num
    total_sum += num
if max_number == total_sum - max_number:
    print(f'Yes \nSum = {max_number}')
else:
    other_sum = total_sum - max_number
    diff_sum = abs(max_number - other_sum)
    print(f'No \nDiff = {diff_sum}')
# print (total_sum)
# print(max_number)
# print(other_sum)
