base_number = int(input())
expected_number = 0

while expected_number != base_number:
    current_number = int(input())
    expected_number += current_number
    if expected_number >= base_number:
        break

print(expected_number)


