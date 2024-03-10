# Да се напише програма, която чете час от денонощието(цяло число) и ден от седмицата(текст)
# - въведени от потребителя и проверява дали офисът на фирма е отворен,
# като работното време на офисът е от 10-18 часа, от понеделник до събота включително
# НЕ СЪМ СВИКНАЛ ДА РАБТЯ В СЪБОТА !!!
hours = int(input())
day = input()
if 10 <= hours <= 18:
    if (day == 'Monday' or day == 'Tuesday' or day == 'Wednesday'
            or day == 'Thursday' or day == 'Friday' or day == 'Saturday'):
        print('open')
    else:
        print('closed')
else:
    print('closed')
