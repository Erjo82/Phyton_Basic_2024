cells = input().split('#')
total_water = int(input())
effort = 0
fire_count_list = []
types_of_fire = ['High', 'Medium', 'Low']
for current_cell in cells:
    type_of_fire, value_of_fire = current_cell.split(' = ')
    value_of_fire = int(value_of_fire)
    is_valid_fire = False
    if type_of_fire == 'High' and value_of_fire in range(81,126):
        is_valid_fire = True
    elif type_of_fire == 'Medium' and value_of_fire in range(51,81):
        is_valid_fire = True
    elif type_of_fire == 'Low' and value_of_fire in range(1,51):
        is_valid_fire = True
    if is_valid_fire:
        if total_water >= value_of_fire:
            total_water -= value_of_fire
            effort += value_of_fire * 0.25
            fire_count_list.append(value_of_fire)
print('Cells:')
for current_fire in fire_count_list:
    print(f' - {current_fire}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(fire_count_list)}')
