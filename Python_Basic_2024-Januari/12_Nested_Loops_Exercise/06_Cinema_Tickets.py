student_ticket = 0
standard_ticket = 0
kid_ticket = 0
research = 0
movies_name = input()

while movies_name != 'Finish':

    free_space = int(input())

    for research in range(1, free_space + 1):
        ticket_type = input()

        if ticket_type == 'student':
            student_ticket += 1
        elif ticket_type == 'standard':
            standard_ticket += 1
        elif ticket_type == 'kid':
            kid_ticket += 1
        if ticket_type == 'End':
            research -= 1
            break

    average_percent = (research / free_space) * 100
    print(f'\n{movies_name} - {average_percent:.2f}% full.', end='')
    movies_name = input()

total_ticket = student_ticket + standard_ticket + kid_ticket
student_percent = (student_ticket / total_ticket) * 100
standard_percent = (standard_ticket / total_ticket) * 100
kid_percent = (kid_ticket / total_ticket) * 100

print(f'Total tickets: {total_ticket}')
print(f'{student_percent:.2f}% student tickets.')
print(f'{standard_percent:.2f}% standard tickets.')
print(f'{kid_percent:.2f}% kids tickets.')
