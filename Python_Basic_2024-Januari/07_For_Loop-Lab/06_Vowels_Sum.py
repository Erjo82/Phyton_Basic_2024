input_text = input()
all_point = 0
for vowels in input_text:
    if vowels == 'a':
        all_point += 1
    elif vowels == 'e':
        all_point += 2
    elif vowels == 'i':
        all_point += 3
    elif vowels == 'o':
        all_point += 4
    elif vowels == 'u':
        all_point += 5
print(all_point)

