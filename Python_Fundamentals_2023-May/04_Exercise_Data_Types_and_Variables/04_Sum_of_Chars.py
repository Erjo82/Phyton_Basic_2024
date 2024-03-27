total_cycle = int(input())
total_sum = 0
for calculation in range(total_cycle):
    current_char = input()
    total_sum += ord(current_char)
print(f'The sum equals: {total_sum}')
