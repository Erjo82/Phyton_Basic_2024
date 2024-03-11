from math import ceil, floor

days = int(input())
left_food = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_kg = float(input()) / 1000

all_needed_food = (dog_food_kg * days) + (cat_food_kg * days) + (turtle_food_kg * days)

if all_needed_food < left_food:
    leftover_food = floor(left_food - all_needed_food)
    print(f'{leftover_food} kilos of food left.')

else:
    needed_food = ceil(all_needed_food - left_food)
    print(f'{needed_food} more kilos of food are needed.')
