tank_capacity = 0
all_received_liters = int(input())
for current_liters in range(all_received_liters):
    liters = int(input())
    tank_capacity += liters
    if tank_capacity > 255:
        tank_capacity -= liters
        print(f'Insufficient capacity!')
print(tank_capacity)