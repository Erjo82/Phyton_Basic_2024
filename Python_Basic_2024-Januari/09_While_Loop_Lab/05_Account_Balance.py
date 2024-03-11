#   --------------- решение 1 --------------
balance = 0
payment = input()

while payment != 'NoMoreMoney':
    current_sum = float(payment)

    if current_sum >= 0:
        balance += current_sum
        print(f'Increase: {current_sum:.2f}')

    else:
        print(f'Invalid operation!')
        break
    payment = input()
print(f'Total: {balance:.2f}')

# ---------------- решение 2 ----------------
# while True:
#     payment = input()
#     if payment == 'NoMoreMoney':
#         break
#
#     current_sum = float(payment)
#
#     if current_sum >= 0:
#         balance += current_sum
#         print(f'Increase: {current_sum:.2f}')
#     else:
#         print(f'Invalid operation!')
#         break
#
# print(f'Total: {balance:.2f}')
