    # 1. Дължина в см – цяло число в интервала [10 … 500]
daljina = int(input())
    # 2. Широчина в см – цяло число в интервала [10 … 300]
shirina = int(input())
    # 3. Височина в см – цяло число в интервала [10… 200]
visochina = int(input())
    # 4. Процент  – реално число в интервала [0.000 … 100.000]
precent = float(input())

obem_akvarum = (daljina * visochina * shirina) /1000
zaeto_prostranstvo = obem_akvarum * (precent / 100)
nujna_voda = obem_akvarum - zaeto_prostranstvo

print(nujna_voda)