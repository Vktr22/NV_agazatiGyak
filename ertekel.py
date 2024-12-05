def hetNapjaBe():
    nap:str=input("\tHét napja: ")
    return nap
def oraNeveBe():
    ora:str = input("\tÓra neve: ")
    return ora
def ertekelBe(min, max):
    ertekeles:int=int(input(f"\tÉrtékelés ({min}-{max}): "))
    while(ertekeles<min or ertekeles>max):
        if (ertekeles<0):
            ertekeles=int(input(f"\tAz értékelés nem lehet negatív!\n\tÉrtékelés ({min}-{max}): "))
        else:
            ertekeles=int(input(f"\t{max} pont feletti értékelés nem elfogadható!\n\tÉrtékelés ({min}-{max}): "))
    return ertekeles