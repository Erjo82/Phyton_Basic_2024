number = int(input())
is_prime = True
for prime_sum_check in range (2, number):
    if number % prime_sum_check == 0:
        is_prime = False
print(is_prime)