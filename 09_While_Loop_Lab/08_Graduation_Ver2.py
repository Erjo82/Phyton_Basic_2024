name = input()
successful_year = 0
unsuccessful_year = 0
all_grades = 0
average_grade = 0

while True:
    annual_grade = float(input())
    if annual_grade < 4:
        unsuccessful_year += 1
        if unsuccessful_year > 1:
            print(f'{name} has been excluded at {successful_year + 1} grade')
            break
        continue
    successful_year += 1
    all_grades += annual_grade
    if successful_year >= 12:
        average_grade = all_grades / 12
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break


