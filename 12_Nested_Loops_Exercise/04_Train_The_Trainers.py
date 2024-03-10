judge_pcs = int(input())
presentation_name = input()
average_count = 0
all_sum = 0

while presentation_name != 'Finish':

    all_student_rating = 0
    for _ in range(judge_pcs):
        student_rating = float(input())
        all_student_rating += student_rating
        all_sum += student_rating
        average_count += 1

    average_student_rating = all_student_rating / judge_pcs
    print(f'\n{presentation_name} - {average_student_rating:.2f}.', end='')
    presentation_name = input()

all_average_rating = all_sum / average_count
print(f"Student's final assessment is {all_average_rating:.2f}.")


