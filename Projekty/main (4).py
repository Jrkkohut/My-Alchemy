import random

def privitanie():
	print("Ahoj, vitaj v mojej hre kameň, papier, nožnice.")


def vstupOdUzivatela():
	while True:
		print("1. kameň")
		print("2. papier")
		print("3. nožnice")
		vstup = input("Zadaj tvoj výber: ").lower()
		if vstup in ["1", "k", "kamen", "kameň"]:
			return "k"
		if vstup in ["2", "p", "papier"]:
			return "p"
		if vstup in ["3", "n", "nožnice", "noznice"]:
			return "n"
		print("Zlá voľba, skús znovu!")


def vstupOdPocitaca():
	return random.choice(['k', 'p', 'n'])

def urciVitaza(clovek, pocitac):
	if pocitac == clovek:
		return 2
	if clovek == "k" and pocitac == "n":
		return 0
	if clovek == "n" and pocitac == "p":
		return 0
	if clovek == "p" and pocitac == "k":
		return 0
	return 1


def hra(vitazne=3):
	privitanie()
	skore = [0, 0, 0] # clovek, pocitac, remiza
	hraci = ["človek", "počítač", "remíza"]
	while True:
		vstup_clovek = vstupOdUzivatela()
		vstup_pocitac = vstupOdPocitaca()
		vitaz = urciVitaza(vstup_clovek, vstup_pocitac)
		skore[vitaz] += 1
		print("Bod pre:", hraci[vitaz], "...", vstup_clovek, vstup_pocitac)
		if skore[0] == vitazne or skore[1] == vitazne:
			break
	print(f"Konečené skóre je {skore[0]} pre človeka, {skore[1]} pre počítač a {skore[2]} remíz.")


hra(3)