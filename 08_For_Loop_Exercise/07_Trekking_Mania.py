nums = int(input())
musala = 0
monblanc = 0
kilimandjaro = 0
k2 = 0
everest = 0
people_count = 0

for climbers in range(nums):
    people = int(input())
    people_count += people
    if people < 6:
        musala += people
    elif people < 13:
        monblanc += people
    elif people < 26:
        kilimandjaro += people
    elif people < 41:
        k2 += people
    else:
        everest += people
musala = musala / people_count * 100
monblanc = monblanc / people_count * 100
kilimandjaro = kilimandjaro / people_count * 100
k2 = k2 / people_count * 100
everest = everest / people_count * 100
print(f'{musala:.2f}%\n{monblanc:.2f}%\n{kilimandjaro:.2f}%\n{k2:.2f}%\n{everest:.2f}%')