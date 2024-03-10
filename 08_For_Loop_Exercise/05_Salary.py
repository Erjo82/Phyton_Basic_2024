open_tabs = int(input())
salary = int(input())

punishment = 0

for _ in range(open_tabs):
    tabs_name = input()

    if tabs_name == 'Facebook':
        punishment += 150

    elif tabs_name == 'Instagram':
        punishment += 100

    elif tabs_name == 'Reddit':
        punishment += 50

    if punishment >= salary:
        print(f'You have lost your salary.')
        break

if salary > punishment:
    left_sum = salary - punishment
    print(f'{left_sum}')
