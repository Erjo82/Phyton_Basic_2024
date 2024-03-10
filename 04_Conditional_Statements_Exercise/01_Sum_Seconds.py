time_of_first = int(input())
time_of_second = int(input())
time_of_third = int(input())

total_time = time_of_first + time_of_second + time_of_third
minutes = total_time // 60
seconds = total_time % 60

print(f'{minutes}:{seconds:02d}')

