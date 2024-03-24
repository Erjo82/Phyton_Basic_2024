word = input()
index_list =[]

for index, letter in enumerate(word):
    if 90 > ord(letter) > 64:
        index_list.append(index)

print(index_list)
