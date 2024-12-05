import ertekel
import hatoslotto
import sorozat

# 1. feladat:
print("I/A, B:")
nap:str = ertekel.hetNapjaBe()
ora:str = ertekel.oraNeveBe()
ertekeles:int = ertekel.ertekelBe(0,5)
print(f"I/C:\n\tKöszönjük az értékelést!\n\tÖsszefoglaló: {nap}, {ora}, {ertekeles} érték")
print("")

# 2. feladat:
print("II/A, B, C:")
velSzLista = sorozat.veletlenSzamokLista(-100, 859, 8)
sorozat.listaKiiratElvalasztva(velSzLista)
print("II/D, E:")
tizOsztDb = sorozat.tizzel_oszthatoak_szama(velSzLista)
sorozat.konzol_ir(tizOsztDb)
print("kimutatas.txt tartalma:\nII/F:")
fajl=sorozat.fajlba_ir(tizOsztDb)
sorozat.txtFileKiirat(fajl)
print("")

# 3. feladat:
lottoLista=hatoslotto.beolvas("huzasok.txt", huzasok_lista=[])
print("III/A, B:")
huzDb=hatoslotto.huzasokSzama(lottoLista)
print(f"A húzások száma: {huzDb}")
print("III/C:")
hetHuzAtl=hatoslotto.adottHetHuzasAtlag(lottoLista, 42)
print(f"\tA 42. héten húzott számok átlaga: {hetHuzAtl}")
print("III/D:")
max=hatoslotto.legnagyobbKihuzottSzam(lottoLista)
hely=hatoslotto.maxHelye(lottoLista, max)
print(f"\tAz első legnagyobb kihúzott szám értéke: {max}, {lottoLista[hely].ev}-ben, a {hely}. héten húzták ki, ez volt a {lottoLista[hely].huzas}.")
