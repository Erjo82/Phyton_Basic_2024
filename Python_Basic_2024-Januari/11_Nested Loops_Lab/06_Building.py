floors = int(input())
rooms = int(input())

for floors_operation in reversed(range(1, floors + 1)):
    if floors_operation == floors:
        room_type = "L"
    elif floors_operation % 2 != 0:
        room_type = 'A'
    else:
        room_type = 'O'

    for rooms_operation in range(rooms):
        room_name = f'{room_type}{floors_operation}{rooms_operation}'
        print(room_name, end=' ')
    print()
