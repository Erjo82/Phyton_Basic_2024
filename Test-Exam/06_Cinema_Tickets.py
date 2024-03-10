student_count = 0
standard_count = 0
kid_count = 0

while True:
    student_ticket = 0
    standard_ticket = 0
    kid_ticket = 0

    movie_name = input()
    if movie_name == 'Finish':
        break
    free_space = int(input())

    for end_free_space in range(1, free_space + 1):
        command = input()
        if command == 'End':
            break
        elif command == 'student':
            student_ticket += 1
            student_count += 1

        elif command == 'standard':
            standard_ticket += 1
            standard_count += 1

        elif command == 'kid':
            kid_ticket += 1
            kid_count += 1

    attendance = ((kid_ticket + standard_ticket + student_ticket) / free_space) * 100
    print(f'\n{movie_name} - {attendance:.2f}% full.', end='')

total_ticket = kid_count + standard_count + student_count
student_percent = (student_count / total_ticket) * 100
standard_percent = (standard_count / total_ticket) * 100
kid_percent = (kid_count / total_ticket) * 100

print(f'\nTotal tickets: {total_ticket}', end='')
print(f'\n{student_percent:.2f}% student tickets.', end='')
print(f'\n{standard_percent:.2f}% standard tickets.', end='')
print(f'\n{kid_percent:.2f}% kids tickets.', end='')
