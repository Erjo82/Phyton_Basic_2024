coffe_count = 0
while True:
    cmd = input()
    if cmd == 'END':
        break
    elif cmd.lower() == 'coding' or cmd.lower() == 'movie' or cmd.lower() == 'dog' or cmd.lower() == 'cat':
        if cmd.isupper():
            coffe_count += 2
        else:
            coffe_count += 1
if coffe_count > 5:
    print('You need extra sleep')
else:
    print(coffe_count)
