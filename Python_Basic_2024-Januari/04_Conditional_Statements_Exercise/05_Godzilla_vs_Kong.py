budget = float(input())
broi_statisti = int(input())
cena_obleklo_1_statist = float(input())

dekor = budget * 0.10

if broi_statisti > 150:
    cena_obleklo_1_statist = cena_obleklo_1_statist * (1 - 0.10)

all_sum = dekor + (cena_obleklo_1_statist * broi_statisti)
money_needet = budget - all_sum

if all_sum > budget:
    print(f'Not enough money!')
    print(f'Wingard needs {abs(money_needet):.2f} leva more.')
else:
    print(f'Action!')
    print(f'Wingard starts filming with {money_needet:.2f} leva left.')

# print(dekor)
# print(cena_obleklo_1_statist)
# print(all_sum)
# print(money_needet)
