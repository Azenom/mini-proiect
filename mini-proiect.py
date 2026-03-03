import json
from functii_ajutor.citire_scriere import functie_citire, validare_cnp, export_csv_filtrat, functie_scriere
from functii_ajutor.gestionare import fluturas, stergere_persoane, modificare_persoane, cauta_persoane, adauga_persoane
from functii_ajutor.meniu_optiuni import functie_meniu


''' Aici reset ---------------------------------'''
# persoane = [{"CNP":"1960101123456","Nume":"Popescu","Prenume":"Andrei","Varsta":29,"Salariu":4500,"Departament":"It","Senioritate":"Mid"},{"CNP":"2950502234567","Nume":"Ionescu","Prenume":"Maria","Varsta":30,"Salariu":5200,"Departament":"Hr","Senioritate":"Senior"},{"CNP":"1980703345678","Nume":"Georgescu","Prenume":"Mihai","Varsta":27,"Salariu":4000,"Departament":"Marketing","Senioritate":"Mid"},{"CNP":"6020814456789","Nume":"Dumitrescu","Prenume":"Elena","Varsta":24,"Salariu":4060,"Departament":"Financiar","Senioritate":"Junior"},{"CNP":"1970905567890","Nume":"Popa","Prenume":"Alexandru","Varsta":33,"Salariu":6000,"Departament":"It","Senioritate":"Senior"},{"CNP":"2961016678901","Nume":"Stan","Prenume":"Ioana","Varsta":28,"Salariu":4700,"Departament":"Vanzari","Senioritate":"Mid"},{"CNP":"1951127789012","Nume":"Marin","Prenume":"Cristian","Varsta":31,"Salariu":5500,"Departament":"Logistica","Senioritate":"Senior"},{"CNP":"2971208890123","Nume":"Voicu","Prenume":"Alina","Varsta":26,"Salariu":4060,"Departament":"It","Senioritate":"Junior"},{"CNP":"1980112991234","Nume":"Morar","Prenume":"Daniel","Varsta":35,"Salariu":6200,"Departament":"Management","Senioritate":"Senior"},{"CNP":"2990213102345","Nume":"Radu","Prenume":"Bianca","Varsta":23,"Salariu":4060,"Departament":"Marketing","Senioritate":"Junior"},{"CNP":"1970314213456","Nume":"Barbu","Prenume":"Paul","Varsta":32,"Salariu":5800,"Departament":"Financiar","Senioritate":"Senior"},{"CNP":"2960415324567","Nume":"Tudor","Prenume":"Raluca","Varsta":27,"Salariu":4200,"Departament":"Hr","Senioritate":"Mid"},{"CNP":"1980516435678","Nume":"Neagu","Prenume":"Vlad","Varsta":30,"Salariu":5100,"Departament":"It","Senioritate":"Mid"},{"CNP":"2990617546789","Nume":"Florea","Prenume":"Diana","Varsta":25,"Salariu":4060,"Departament":"Vanzari","Senioritate":"Junior"},{"CNP":"1960718657890","Nume":"Preda","Prenume":"Sorin","Varsta":34,"Salariu":6100,"Departament":"Logistica","Senioritate":"Senior"},{"CNP":"2970819768901","Nume":"Enache","Prenume":"Laura","Varsta":26,"Salariu":4060,"Departament":"Financiar","Senioritate":"Junior"},{"CNP":"1950920879012","Nume":"Ilie","Prenume":"Gabriel","Varsta":36,"Salariu":6500,"Departament":"Management","Senioritate":"Senior"},{"CNP":"2981021980123","Nume":"Mihalache","Prenume":"Adina","Varsta":28,"Salariu":4400,"Departament":"Marketing","Senioritate":"Mid"},{"CNP":"1971122091234","Nume":"Sandu","Prenume":"Robert","Varsta":31,"Salariu":5700,"Departament":"It","Senioritate":"Senior"},{"CNP":"2991223102345","Nume":"Lazar","Prenume":"Monica","Varsta":24,"Salariu":4060,"Departament":"Hr","Senioritate":"Senior"}]
# functie_scriere(persoane)
'''---------------------------------'''

def cauta_persoane_wrapper() -> None:
    """
    Cere utilizatorului CNP-ul, validează și apelează functia cauta_persoane.
    Continuă să ceară CNP până când se introduce unul valid.
    """
    while True:
        cnp: str = input("Introdu CNP-ul cautat: ")
        if validare_cnp(cnp):
            cauta_persoane(cnp)
            break

def modificare_persoane_wrapper() -> None:
    """
    Cere CNP-ul persoanei de modificat, validează și apelează modificare_persoane.
    Continuă până când se introduce un CNP valid.
    """
    while True:
        cnp: str = input("Introdu CNP-ul persoanei de modificat: ")
        if validare_cnp(cnp) :
            modificare_persoane(cnp)
            break
        else :
            print("CNP-ul trebuie sa aibe 13 cifre !")

def stergere_persoane_wrapper() -> None:
    """
    Cere CNP-ul persoanei de șters, validează și apelează stergere_persoane.
    Continuă până când se introduce un CNP valid.
    """
    while True:
        cnp: str = input("Introdu CNP-ul persoanei de șters: ")
        if validare_cnp(cnp):
            stergere_persoane(cnp)
            break
        else:
            print("CNP invalid! Trebuie să aibă 13 cifre.")

def calcul_total() -> float:
    """
    Calculeaza si afiseaza suma tuturor salariilor angajatilor din companie.
    """
    date = functie_citire()
    suma = 0
    for elem in date:
        suma += elem["Salariu"]
    return suma

def calcul_dep() -> None:
    """
    Calculeaza si afiseaza salariile totale pe fiecare departament.
    """
    date = functie_citire()
    sal_dep={}
    for elem in date :
        dep = elem["Departament"]
        sal = elem["Salariu"]
        if dep not in sal_dep:
            sal_dep[dep] = 0
        sal_dep[dep] += sal
    for dep, total in sal_dep.items():
        print(f'Departamentul : {dep} are {total} ron in salarii')

def fluturas_wrapper() -> None:
    """
    Cere CNP-ul persoanei pentru fluturaș, validează și apelează fluturas.
    Continuă până când se introduce un CNP valid.
    """
    while True:
        cnp: str = input("Introdu CNP-ul pentru fluturas: ")
        if validare_cnp(cnp):
            fluturas(cnp)
            break

def seniori() -> None:
    """
    Creeaza CSV cu angajatii filtrati dupa senioritate.
    """
    date = functie_citire()
    lista=[]
    for elem in date : 
        lista.append(elem['Senioritate'])
    print('Senioritatile disponibile sunt : ',set(lista))
    cauta = input("Introdu senioritatea: ")
    export_csv_filtrat(date, 'Senioritate', cauta, 'fisiere_output/senioritate.csv')

def depart() -> None:
    """
    Creeaza CSV cu angajatii filtrati dupa departament.
    """
    date = functie_citire()
    lista=[]
    for elem in date : 
        lista.append(elem['Departament'])
    print('Departamentele disponibile sunt : ',set(lista))
    cauta = input("Introdu departamentul: ")
    export_csv_filtrat(date, 'Departament', cauta, 'fisiere_output/departament.csv')

# Meniul principal ------------------------------------------------------
functie_meniu()
while True :
    optiune = input("Alege optiune : ")
    if optiune == '0' :
        print("Ai iesit din sistem ! ")
        break
    if optiune == "1" :
        adauga_persoane()
    if optiune == "2" :
        cauta_persoane_wrapper()
    if optiune == "3" :
        modificare_persoane_wrapper()
    if optiune == '4' :
        stergere_persoane_wrapper()
    if optiune == '5' :
        date = functie_citire()
        print(json.dumps(date, indent=4))
    if optiune == '6' :
        print('Calcul cost total salarii companie : ',calcul_total())
    if optiune == '7' :
        calcul_dep()
    if optiune == '8' :
        fluturas_wrapper()
    if optiune == '9' :
        seniori()
    if optiune == '10':
        depart()