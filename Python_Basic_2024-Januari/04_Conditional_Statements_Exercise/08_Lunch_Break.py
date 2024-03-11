from math import ceil

name_of_serials = input()
length_of_serial = int(input())
length_of_rest = int(input())
time_of_lunch = (1 / 8) * length_of_rest
time_of_recreation = (1 / 4) * length_of_rest
time_left = length_of_rest - time_of_recreation - time_of_lunch

if time_left >= length_of_serial:
    time_left_to_watch = time_left - length_of_serial
    print(
        f'You have enough time to watch {name_of_serials} and left with {ceil(time_left_to_watch)} minutes free time.')
else:
    time_needed_to_watch = length_of_serial - time_left
    print(f"You don't have enough time to watch {name_of_serials}, you need {ceil(time_needed_to_watch)} more minutes.")
