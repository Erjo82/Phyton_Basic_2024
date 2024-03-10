budged = float(input())
season = input()
destination = ''
trip_budget = 0
camp_or_hotel = ''

if budged <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        camp_or_hotel = 'Camp'
        trip_budget = budged * 0.30
    else:
        trip_budget = budged * 0.7
        camp_or_hotel = 'Hotel'

elif budged <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        camp_or_hotel = 'Camp'
        trip_budget = budged * 0.4
    else:
        trip_budget = budged * 0.8
        camp_or_hotel = 'Hotel'


elif budged > 1000:
    destination = 'Europe'
    camp_or_hotel = 'Hotel'
    trip_budget = budged * 0.9

print(f'Somewhere in {destination}')
print(f'{camp_or_hotel} - {trip_budget:.2f}')

