input_day_off = int(input())
needed_time = 30_000

all_days = ((365 - input_day_off) * 63) + (input_day_off * 127)
diff = abs(needed_time - all_days)
diff_in_hour = diff // 60
diff_in_min = diff % 60

if needed_time > all_days:
    print(f'Tom sleeps well')
    print(f'{diff_in_hour} hours and {diff_in_min} minutes less for play')
else:
    print(f'Tom will run away')
    print(f'{diff_in_hour} hours and {diff_in_min} minutes more for play')

# print(day_off)
# print(diff)
# print(diff_in_hour)
# print(diff_in_min)
