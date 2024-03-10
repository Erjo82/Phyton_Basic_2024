wins = 0
loses = 0
all_match = 0

while True:
    tournament_name = input()
    if tournament_name == 'End of tournaments':
        break
    total_match = int(input())
    for calculation in range(1, total_match + 1):
        home_score = int(input())
        guest_score = int(input())

        if home_score > guest_score:
            wins += 1
            win_diff = home_score - guest_score
            print(f'Game {calculation} of tournament {tournament_name}: win with {win_diff} points.')
        else:
            loses += 1
            lose_diff = guest_score - home_score
            print(f'Game {calculation} of tournament {tournament_name}: lost with {lose_diff} points.')
        all_match += 1
average_wins = (wins / all_match) * 100
average_loses = (loses / all_match) * 100

print(f'{average_wins:.2f}% matches win')
print(f'{average_loses:.2f}% matches lost')
