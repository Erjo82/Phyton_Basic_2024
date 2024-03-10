skumria_1_kilo = float(input())
caca_1_kilo = float(input())
kilograma_palamud = float(input())
kilograma_safrid = float(input())
midi_kilo = float(input()) * 7.5
palamud_cena = skumria_1_kilo * (1 + 0.60) * kilograma_palamud
safrid_cena = caca_1_kilo * (1 + 0.8) * kilograma_safrid
all_sum = palamud_cena + safrid_cena + midi_kilo

print(f'{all_sum:.2f}')

