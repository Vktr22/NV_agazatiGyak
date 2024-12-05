import random


def veletlenSzamokLista(min, max, dbElem):
    velSzLista=[]
    i=0
    while (i<dbElem):
        elem:int=int(random.random()*(max-min+1)+min)
        velSzLista.append(elem)
        i+=1
    return velSzLista

def listaKiiratElvalasztva(lista):
    i=0
    while(i<(len(lista)-1)):
        print(lista[i], end=";")
        i+=1
    print(lista[i])

def tizzel_oszthatoak_szama(lista):
    db:int = 0
    i=0
    while(i<len(lista)):
        if (lista[i]%10==0):
            db+=1
        i+=1
    return db

def konzol_ir(db):
    print(f"\tTízzel osztható számok Száma: {db}")

'''
A tizzel_osztahatoak_szama függvény eredményét írassa ki
a mintának megfelelően a vegeredmeny.txt nevű fájlba,
amit fajlba_ir nevű metódusban fogalmazzon meg! 
'''
def fajlba_ir(db):
    vegeredmenyTxt = open("vegeredmeny.txt", "w", encoding="UTF-8")
    vegeredmenyTxt.write(f"Tízzel osztható számok Száma: {db}")
    vegeredmenyTxt.close()

def txtFileKiirat(file):
    file = open("vegeredmeny.txt", "r", encoding="UTF-8")
    print(f"\t{file.read()}")



