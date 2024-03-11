# ---------------easy way
# divisor = int(input())
# boundary = int(input())
#
# for current_number in range(boundary, divisor - 1, -1):
#     if current_number % divisor == 0:
#         print(current_number)
#         break
# --------------hard way

# divisor = int(input())
# boundary = int(input())
# list_of_number = []
# for current_number in range(divisor, boundary + 1):
#     if current_number % divisor == 0:
#         list_of_number.append(current_number)
# print(list_of_number[len(list_of_number) - 1])
# ---------------last way

divisor = int(input())
boundary = int(input())
max_num = 0
for current_number in range(divisor, boundary + 1):
    if current_number % divisor == 0:
       max_num = current_number
print(max_num)