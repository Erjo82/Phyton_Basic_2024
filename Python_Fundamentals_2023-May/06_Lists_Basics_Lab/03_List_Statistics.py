total_number = int(input())
positive_number = []
negative_number = []
for current_number in range(total_number):
    numbers = int(input())
    if numbers >= 0:
        positive_number.append(numbers)
    else:
        negative_number.append(numbers)
print(positive_number)
print(negative_number)
print(f'Count of positives: {len(positive_number)}')
print(f'Sum of negatives: {sum(negative_number)}')
