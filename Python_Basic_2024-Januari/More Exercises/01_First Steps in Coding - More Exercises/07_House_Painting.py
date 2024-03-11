visochina_kashta = float(input())
daljina_kashta = float(input())
visochina_triagalen_pokriv = float(input())

stranichni_steni = (visochina_kashta * daljina_kashta) * 2
prozorec = 2.25 * 2
predni_zadni_steni = ((visochina_kashta ** 2) * 2) - 2.4
all_steni = (stranichni_steni - prozorec + predni_zadni_steni) / 3.4
pokriv = (((visochina_kashta * daljina_kashta) * 2) + (2 * (visochina_kashta * visochina_triagalen_pokriv) / 2)) / 4.3

print(f'{all_steni:.2f}')
print(f'{pokriv:.2f}')
