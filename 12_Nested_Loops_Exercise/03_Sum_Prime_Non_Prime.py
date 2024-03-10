command = input()
prime_numbers_sum = 0
nonprime_numbers_sum = 0

while command != 'stop':
    number = int(command)

    if number < 0:
        print('Number is negative.')
        command = input()
        continue



    if is_prime:
        prime_numbers_sum += number

    else:
        nonprime_numbers_sum += number

    command = input()

print(f'Sum of all prime numbers is: {prime_numbers_sum}')
print(f'Sum of all non prime numbers is: {nonprime_numbers_sum}')
