ime_na_student = input()
neuspeshni_godini = 0
zavarsheni_klasove = 0
obshta_ocenka = 0

while zavarsheni_klasove < 12:
    godishna_ocenka = float(input())
    if godishna_ocenka < 4:
        neuspeshni_godini += 1
        if neuspeshni_godini > 1:
            print(f'{ime_na_student} has been excluded at {zavarsheni_klasove + 1} grade') # принтрва в кой клас го изключват
            break
        continue
    obshta_ocenka += godishna_ocenka
    zavarsheni_klasove += 1
else:
    sredna_ocenka = obshta_ocenka / 12
    print(f'{ime_na_student} graduated. Average grade: {sredna_ocenka:.2f}')
