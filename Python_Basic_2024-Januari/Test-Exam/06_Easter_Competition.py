total_evaluation = int(input())
best_score = 0
best_player = ''
is_new_best_player = False
print()

for evaluation in range(1, total_evaluation + 1):
    judge_score = 0
    player_name = input()

    while True:
        command = input()
        if command == 'Stop':
            if judge_score > best_score:
                best_score = judge_score
                best_player = player_name
                is_new_best_player = True
            break

        judge_point = int(command)
        judge_score += judge_point

    print(f'{player_name} has {judge_score} points.')
    if is_new_best_player:
        print(f'{best_player} is the new number 1!')
        is_new_best_player = False
print(f'{best_player} won competition with {best_score} points!')