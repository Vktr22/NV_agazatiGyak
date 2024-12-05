from Huzas import Huzas

def beolvas(fajlnev,huzasok_lista=[]):
    fajlom=open(fajlnev,"r", encoding="UTF-8")
    elso_sor=fajlom.readline()
    tobbi_sor_lista=fajlom.readlines()

    for i in range(0,len(tobbi_sor_lista),1):
        sor=tobbi_sor_lista[i].strip()
        sor_lista=sor.split("@")
        huzas=Huzas(sor_lista[0],sor_lista[1],sor_lista[2],sor_lista[3])
        huzasok_lista.append(huzas)
    fajlom.close()
    return huzasok_lista

def huzasokSzama(lista):
    #lista[0].huzas
    i:int = 0
    huzDb:int = 0
    for i in range(0, len(lista),1):
        huzDb+=1
    return huzDb

def adottHetHuzasAtlag(lista, melyikHet):
    db:int=0
    atlag:float=0
    for i in range(0, len(lista), 1):
        if(lista[i].het == melyikHet):
            db+=1
            atlag+=lista[i].szam
    atlag=atlag/db
    return atlag

def legnagyobbKihuzottSzam(lista):
    max:int=0
    for i in range(0,len(lista),1):
        if(lista[i].szam>max):
            max=lista[i].szam
    return max

def maxHelye(lista, max):
    helye:int=0
    i:int=0
    while(lista[i].szam!=max):
        if (lista[i].szam == max):
            helye=i
        i+=1
    return helye

