import sys
min_number = sys.maxsize

while True:
    number = input()
    if number == 'Stop':
        break
    current_number = int(number)
    if current_number < min_number:
        min_number = current_number

print(min_number)

