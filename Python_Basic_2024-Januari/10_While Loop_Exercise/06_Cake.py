width = int(input())
length = int(input())
all_pcs = width * length

while all_pcs > 0:
    command_or_cake_pcs = input()
    if command_or_cake_pcs == 'STOP':
        break
    command_or_cake_pcs = int(command_or_cake_pcs)
    all_pcs -= command_or_cake_pcs

if all_pcs > 0:
    print(f'{all_pcs} pieces are left.')
else:
    print(f'No more cake left! You need {abs(all_pcs)} pieces more.')



