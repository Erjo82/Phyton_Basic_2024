factor_number = int(input())
count_number = int(input())
result_number_list = []
for current_calculation in range(1, count_number + 1):
    result_number_list.append(current_calculation * factor_number)
print(result_number_list)