group_size = int(input())
adventures_day = int(input())
earned_coins = 0
for current_day in range(1, adventures_day +1):
    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5
    if current_day % 5 == 0:
        earned_coins += 20 * group_size
        if current_day % 3 == 0:
            earned_coins -= 2 * group_size
    if current_day % 3 == 0:
        earned_coins -= 3 * group_size
    earned_coins += 50
    earned_coins -= 2 * group_size
earned_coins = earned_coins // group_size
print(f'{group_size} companions received {earned_coins} coins each.')
