how_many_numbers = int(input())
for numbers in range(how_many_numbers):
    current_number = int(input())
    if current_number % 2 != 0:
        print(f'{current_number} is odd!')
        break

else:
    print('All numbers are even.')
