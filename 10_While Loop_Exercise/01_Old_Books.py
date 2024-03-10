book_name = input()
counter = 0
command = input()

while command != 'No More Books':

    if command == book_name:
        print(f'You checked {counter} books and found it.')
        break
    counter += 1
    command = input()

if command == 'No More Books':
    print(f'The book you search is not here!')
    print(f'You checked {counter} books.')

