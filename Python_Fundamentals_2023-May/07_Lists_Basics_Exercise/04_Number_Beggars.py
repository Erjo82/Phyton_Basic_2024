offers_str = input().split(', ')
beggars = int(input())
offers_int = []
for change in offers_str:
    offers_int.append(int(change))
start_index = 0
collected_sum = []

while start_index < beggars:
    sum_of_current_beggars = 0
    for current_beggars in range(start_index, len(offers_int), beggars):
        sum_of_current_beggars += offers_int[current_beggars]
    collected_sum.append(sum_of_current_beggars)
    start_index += 1

print(collected_sum)