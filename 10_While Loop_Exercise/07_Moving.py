width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())
needed_space = 0
command = input()

free_space_total = shirina_free_space * daljina_free_space * visochina_free_space

while command != 'Done':
    command = int(command)
    needed_space += command
    if needed_space > free_space_total:
        break
    command = input()

diff = abs(free_space_total - needed_space)

if free_space_total < needed_space:
    print(f'No more free space! You need {diff} Cubic meters more.')

else:
    print(f'{diff} Cubic meters left.')

