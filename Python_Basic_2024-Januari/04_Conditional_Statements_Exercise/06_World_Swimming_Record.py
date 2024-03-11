from math import floor

record_in_seconds = float(input())
range_in_meeters = float(input())
time_in_seconds_per_1_meter = float(input())

time_needet_to_swim = range_in_meeters * time_in_seconds_per_1_meter
zabaviane = (floor(range_in_meeters / 15)) * 12.5
total_time = time_needet_to_swim + zabaviane

if total_time < record_in_seconds:

    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    seconds_needet = total_time - record_in_seconds
    print(f'No, he failed! He was {seconds_needet:.2f} seconds slower.')
