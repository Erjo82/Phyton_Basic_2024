total_string = int(input())
searching_word = input()
string_list = []
for all_string in range(total_string):
    current_string = input()
    string_list.append(current_string)
print(string_list)
for index_in_list in range(len(string_list) -1, -1, -1):
    if searching_word not in string_list[index_in_list]:
        string_list.remove(string_list[index_in_list])
print(string_list)
