number = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for histogram in range(number):
    nums = int(input())
    if nums < 200:
        p1_count += 1

    elif nums < 400:
        p2_count += 1

    elif nums < 600:
        p3_count += 1

    elif nums < 800:
        p4_count += 1

    else:
        p5_count += 1
        pass
p1_count = p1_count / number * 100
p2_count = p2_count / number * 100
p3_count = p3_count / number * 100
p4_count = p4_count / number * 100
p5_count = p5_count / number * 100
print(f'{p1_count:.2f}%\n{p2_count:.2f}%\n{p3_count:.2f}%\n{p4_count:.2f}%\n{p5_count:.2f}%')
