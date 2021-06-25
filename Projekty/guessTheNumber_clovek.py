"""
háda človek
========
počítač si myslí číslo => random od 0 po 100
ak hodnota čo človek hádal == hodnote => správne
ak hodnota čo človek hádal > hodnota => menšie
ak hodnota čo človek hádal < hodnota => väčšie
"""
import random


def hodnota_pc():
	return random.randint(0, 100)


def hodnota_clovek():
	cislo = input("Hádaj číslo: ")
	return int(cislo)


def porovnaj(hodnota_pc, hodnota_clovek):
	if hodnota_pc == hodnota_clovek:
		print("Správne")
		return True
	elif hodnota_clovek > hodnota_pc:
		print("Menšie")
	elif hodnota_clovek < hodnota_pc:
		print("Väčšie")


def hra():
	hod_pc = hodnota_pc()
	cnt = 0
	while True:
		cnt += 1
		hod_clovek = hodnota_clovek()
		vysledok = porovnaj(hod_pc, hod_clovek)
		if vysledok:
			break
	print(f"Uhádol si na {cnt} pokus!")

hra()