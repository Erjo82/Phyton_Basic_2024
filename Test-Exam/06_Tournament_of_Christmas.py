days = int(input())
price = 0
day_price = 0
day_win = 0
day_lose = 0
all_games_win = 0
is_winner = False

for games_in_day in range(days):
    win = 0
    lose = 0
    price = 0
    game_type = input()

    while game_type != 'Finish':

        win_or_lose = input()
        if win_or_lose == 'win':
            price += 20
            win += 1
            day_win += 1
        else:
            lose += 1
            day_lose += 1

        game_type = input()

    if win > lose:
        day_price += int(price * 1.10)

    else:
        day_price += price

if day_win > day_lose:
    is_winner = True
    all_games_win = day_price * 1.20

if is_winner:
    print(f'You won the tournament! Total raised money: {all_games_win:.2f}')

else:
    print(f'You lost the tournament! Total raised money: {day_price:.2f}')

