all_gifts = input().split()

while True:
    command = input().split()
    if command[0] == 'No' and command[1] == 'Money':
        break
    elif command[0] == 'OutOfStock':
        for index, current_gift in enumerate(all_gifts):
            if current_gift == command[1]:
                all_gifts[index] = 'None'
        count = 0
    elif command[0] == 'Required':
        for index2, current_gift2 in enumerate(all_gifts):
            if index2 == int(command[2]):
                all_gifts[index2] = command[1]
    elif command[0] == 'JustInCase':
        all_gifts[-1] = command[1]

for print_gift in all_gifts:
    if print_gift == 'None':
        continue
    else:
        print(print_gift, end=' ')
