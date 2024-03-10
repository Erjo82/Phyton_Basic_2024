target_steps = 10_000
all_steps = 0

while all_steps < target_steps:
    command = input()
    if command == 'Going home':
        final_steps = int(input())
        all_steps += final_steps
        break

    command = int(command)
    all_steps += command

if all_steps >= target_steps:
    diff = all_steps - target_steps
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')

else:
    diff = target_steps - all_steps
    print(f'{diff} more steps to reach goal.')
