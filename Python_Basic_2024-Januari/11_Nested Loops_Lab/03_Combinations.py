num = int(input())
num_counter = 0
for num1 in range(0, num + 1):
    for num2 in range(0, num + 1):
        for num3 in range(0, num + 1):
            if num1 + num2 + num3 == num:
                num_counter += 1
print(num_counter)
