year = int(input())

while True:
    year += 1
    number_list = []
    for current_year in str(year):
        number_list.append(current_year)
    for second_year in str(year):
        if second_year not in number_list:
