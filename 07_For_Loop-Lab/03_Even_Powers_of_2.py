number = int(input())
for cycle in range(number + 1):
    if cycle % 2 == 0:
        cycle_number = 2 ** cycle
        print(cycle_number)
