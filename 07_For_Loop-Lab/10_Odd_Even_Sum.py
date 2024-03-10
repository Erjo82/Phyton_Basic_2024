number = int(input())
even = 0
odd = 0

for operation in range(number):
    sums = int(input())
    if operation % 2 == 0:  # ------------ Odd -------------
        even += sums
    else:  # ------------ Even -------------
        odd += sums
if even == odd:
    print(f'Yes \nSum = {even}')
else:
    diff = abs(even - odd)
    print(f'No \nDiff = {diff}')
