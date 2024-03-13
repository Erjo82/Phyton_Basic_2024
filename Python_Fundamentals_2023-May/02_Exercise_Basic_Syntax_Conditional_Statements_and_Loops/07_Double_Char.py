while True:
    command = input()
    if command == 'End':
        break
    elif command == 'SoftUni':
        continue
    for character_of_current_command in command:
        print(character_of_current_command * 2, end='')
    print()


