
"""
háda počítač
=======
počítač háda číslo
"""


def stredne_cislo(min, max):
	cislo = (min+max) // 2
	return cislo


def interpolate(lst, value, from_, to_, cnt=0):
	if lst[from_] == value:
		return from_
	if from_ == to_ or lst[from_] == lst[to_]:
		return -1
	index = int(from_ + ((to_ - from_)/(lst[to_] - lst[from_]) * (value - lst[from_])))
	if lst[index] == value:
		return index
	if lst[index] < value:
		return interpolate(lst, value, index + 1, to_, cnt+1)
	return interpolate(lst, value, from_, index - 1, cnt+1)


def kontrola_od_uzivatela(cislo):
	print(f"Počítač háda číslo {cislo}")
	odpoved = input("Zádaj väčšie [v], menšie [m], rovné [r]: ").lower()
	if odpoved in ["väčšie", "vacsie", "v"]:
		return 1
	if odpoved in ["menšie", "mensie", "m"]:
		return -1
	if odpoved in ["rovné", "rovne", "r"]:
		return 0


def hra():
	min, max = 0, 100
	cnt = 0
	while True:
		cnt += 1
		cislo = stredne_cislo(min, max)
		kontrola = kontrola_od_uzivatela(cislo)
		if kontrola == 0:
			break
		if kontrola == -1:
			max = cislo
		else:
			min = cislo

	print(f"Počítač uhádol na {cnt} pokus.")

import time
lst = [i for i in range(0, 100000001, 2)]
from_ = 0
to_ = len(lst)
value = 132456

start = time.time()
print(interpolate(lst, value, from_, to_-1))
end = time.time()
print("interpolate", end - start)

start = time.time()
print(lst.index(value))
end = time.time()
print("index", end - start)