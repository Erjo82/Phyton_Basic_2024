all_card = input().split()
total_shuffle = int(input())
half_card = int(len(all_card) / 2)
after_shuffle_card = []
for all_shuffle in range(total_shuffle):
    left_side_of_card = all_card[:half_card]
    right_side_of_card = all_card[half_card:]
    for current_shuffle in range(half_card):
        after_shuffle_card.append(left_side_of_card[current_shuffle])
        after_shuffle_card.append(right_side_of_card[current_shuffle])
    all_card = after_shuffle_card
    after_shuffle_card = []
print(all_card)
