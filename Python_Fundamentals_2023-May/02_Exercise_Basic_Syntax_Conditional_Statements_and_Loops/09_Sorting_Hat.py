is_voldemort = False
while True:
    name = input()
    if name == 'Welcome!':
        break
    elif name == 'Voldemort':
        is_voldemort = True
        break
    elif len(name) < 5:
        print(f'{name} goes to Gryffindor.')
    elif len(name) == 5:
        print(f'{name} goes to Slytherin.')
    elif len(name) == 6:
        print(f'{name} goes to Ravenclaw.')
    elif len(name) > 6:
        print(f'{name} goes to Hufflepuff.')
if is_voldemort:
    print('You must not speak of that name!')
else:
    print('Welcome to Hogwarts.')
