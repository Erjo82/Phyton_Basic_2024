operations_pcs = int(input())
first_all_sum = 0
second_all_sum = 0

for operation_1_1 in range(operations_pcs):
    left_sum = int(input())
    first_all_sum = first_all_sum + left_sum

for operation_1_2 in range(operations_pcs):
    right_sum = int(input())
    second_all_sum += right_sum

if first_all_sum == second_all_sum:
    print(f'Yes, sum = {abs(first_all_sum)}')
else:
    print(f'No, diff = {abs(first_all_sum - second_all_sum)}')
