dagree = float(input())

if dagree <= 35 and dagree >= 26:
    print('Hot')
elif dagree <= 25.9 and dagree >= 20.1:
    print('Warm')
elif dagree <= 20 and dagree >= 15:
    print('Mild')
elif dagree <= 14.9 and dagree >= 12:
    print('Cool')
elif dagree <= 11.9 and dagree >= 5:
    print('Cold')
else:
    print(f'unknown')
