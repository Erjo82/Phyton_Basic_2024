total_line = int(input())
left_bracket = 0
right_bracket = 0
for current_line in range(total_line):
    line = input()
    left_bracket += line.count('(')
    right_bracket += line.count(')')
if left_bracket == right_bracket:
    print('BALANCED')
else:
    print('UNBALANCED')
