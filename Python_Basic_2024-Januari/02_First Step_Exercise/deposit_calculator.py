# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
deposirana_suma = float(input())
srok_deposit = int(input())
lihven_procent = float(input())
lihva_suma = lihven_procent / 100
formula = deposirana_suma + srok_deposit * ((deposirana_suma * lihva_suma) / 12)

print(formula)
