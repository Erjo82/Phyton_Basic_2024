username = input()
password = input()

compare_password = input()

while compare_password != password:
    compare_password = input()
print(f'Welcome {username}!')
