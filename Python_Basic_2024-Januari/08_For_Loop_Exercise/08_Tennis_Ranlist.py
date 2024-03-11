tournaments = int(input())
start_point = int(input())
earning_point = 0
wins_count = 0

for _ in range(tournaments):
    performance = input()

    if performance == 'W':
        wins_count += 1
        earning_point += 2000

    elif performance == 'F':
        earning_point += 1200

    elif performance == 'SF':
        earning_point += 720

final_point = start_point + earning_point
average_points = int(earning_point / tournaments)
wins_percent = (wins_count / tournaments) * 100

print(f'Final points: {final_point}')
print(f'Average points: {average_points}')
print(f'{wins_percent:.2f}%')
