name_actor = input()
all_point = float(input())
judge = int(input())
barrier_point = 1250.5

for _ in range(judge):
    name_of_judge = input()
    point_from_judge = float(input())
    point = (len(name_of_judge) * point_from_judge) / 2
    all_point += point
    if all_point > barrier_point:
        break

if all_point > barrier_point:
    print(f'\nCongratulations, {name_actor} got a nominee for leading role with {all_point:.1f}!')

else:
    needed_point = barrier_point - all_point
    print(f'Sorry, {name_actor} you need {needed_point:.1f} more!')
