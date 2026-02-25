"""
Sa se scrie un program care tine evidenta angajatilor dintr-o companie.
Informatiile pe care trebuie sa le retinem despre un angajat sunt urmatoarele:
	1) CNP
	2) Nume
	3) Prenume
	4) Varsta
	5) Salar
	6) Departament
	7) Senioritate (junior, mid, senior)

Programul trebuie sa dispuna de un meniu care ne permite sa efectuam urmatoarele actiuni:
	1) Adaugare angajat                          - in prog
	2) Cautare angajat (dupa CNP)                - in fisier
	3) Modificare date angajat (dupa CNP)        - in fisier
	4) Stergere angajat (dupa CNP)               - in fisier
	5) Afisare angajati                          - din fisier
	6) Calcul cost total salarii companie        - in prog
	7) Calcul cost total salarii departament     - in prog
	8) Calcul fluturas salar angajat (dupa CNP)  - in fisier .py ( modul )
    Formula : Salariu Net = Salariu Brut - CAS (25%) - CASS (10%) - Impozit ( 10% din (Salariu Brut - CAS (25%) - CASS (10%) ) )
    9) Afisarea angajatilor pe baza senioritatii - in fisier
	10) Afisarea angajatilor pe baza departamentului - in fisier
	11) Iesire

Informatiile despre angajati trebuie sa fie stocate intr-un fisier astfel incat sa poata fi accesate si modificate ulterior.

Criterii notare:
    - 0.5p  documentare cod (docstrings, comentarii)
    - 0.5p  type hints
    - 1p    modularitate (impartirea codului in functii, module, etc)
    - 1p    naming conventions (denumire variabile, denumire functii, etc)
    - 1p    error handling (try-except, validare integritate date *, etc)
    - 1p    salvarea datelor intr-un fisier (citire/scriere) - punctul 9, 10
    - 0.5p  adaugare angajati
    - 0.5p  afisare angajati
    - 0.5p  cautare angajat
    - 0.5p  modificare date angajat
    - 0.5p  stergere angajat
    - 0.5p  calcul cost total salarii companie
    - 0.5p  calcul cost total salarii departament
    - 0.5p  calcul fluturas salarial
    - 0.5p  afisarea angajatilor pe baza senioritatii
    - 0.5p  afisarea angajatilor pe baza departamentului

	* Verificare integriatate date (parametrii introdusi sa fie corespunzatori)
		- Exemple:
			- CNP sa fie de lungime corespunzatoare si sa contina doar cifre
			- Varsta sa fie mai mare de 18 ani
			- Salarul sa fie mai mare decat minimul pe economie (4050)
			- etc

Termen limita: Sambata 6 martie 2026 ora 23:59
Lucrul in echipa pentru acest proiect este permis, dar fiecare membru trebuie sa predea o versiune individuala a proiectului,
care sa fie diferita de cea a colegilor sai (de exemplu, prin adaugarea unor functionalitati suplimentare sau prin implementarea intr-un mod diferit a functionalitatilor cerute).
Pentru persoanele care depasesc termenul limita se vor scadea cate 0.25p pentru fiecare zi de intarziere.
Maximul de zile de intarziere este de 14 zile, dupa care proiectul nu va mai fi acceptat, iar nota va fi 1.
"""

import json
persoane = [{"CNP":"1960101123456","Nume":"Popescu","Prenume":"Andrei","Varsta":29,"Salar":4500,"Departament":"IT","Senioritate":"mid"},{"CNP":"2950502234567","Nume":"Ionescu","Prenume":"Maria","Varsta":30,"Salar":5200,"Departament":"HR","Senioritate":"senior"},{"CNP":"1980703345678","Nume":"Georgescu","Prenume":"Mihai","Varsta":27,"Salar":4000,"Departament":"Marketing","Senioritate":"mid"},{"CNP":"6020814456789","Nume":"Dumitrescu","Prenume":"Elena","Varsta":24,"Salar":3500,"Departament":"Financiar","Senioritate":"junior"},{"CNP":"1970905567890","Nume":"Popa","Prenume":"Alexandru","Varsta":33,"Salar":6000,"Departament":"IT","Senioritate":"senior"},{"CNP":"2961016678901","Nume":"Stan","Prenume":"Ioana","Varsta":28,"Salar":4700,"Departament":"Vanzari","Senioritate":"mid"},{"CNP":"1951127789012","Nume":"Marin","Prenume":"Cristian","Varsta":31,"Salar":5500,"Departament":"Logistica","Senioritate":"senior"},{"CNP":"2971208890123","Nume":"Voicu","Prenume":"Alina","Varsta":26,"Salar":3800,"Departament":"IT","Senioritate":"junior"},{"CNP":"1980112991234","Nume":"Morar","Prenume":"Daniel","Varsta":35,"Salar":6200,"Departament":"Management","Senioritate":"senior"},{"CNP":"2990213102345","Nume":"Radu","Prenume":"Bianca","Varsta":23,"Salar":3400,"Departament":"Marketing","Senioritate":"junior"},{"CNP":"1970314213456","Nume":"Barbu","Prenume":"Paul","Varsta":32,"Salar":5800,"Departament":"Financiar","Senioritate":"senior"},{"CNP":"2960415324567","Nume":"Tudor","Prenume":"Raluca","Varsta":27,"Salar":4200,"Departament":"HR","Senioritate":"mid"},{"CNP":"1980516435678","Nume":"Neagu","Prenume":"Vlad","Varsta":30,"Salar":5100,"Departament":"IT","Senioritate":"mid"},{"CNP":"2990617546789","Nume":"Florea","Prenume":"Diana","Varsta":25,"Salar":3600,"Departament":"Vanzari","Senioritate":"junior"},{"CNP":"1960718657890","Nume":"Preda","Prenume":"Sorin","Varsta":34,"Salar":6100,"Departament":"Logistica","Senioritate":"senior"},{"CNP":"2970819768901","Nume":"Enache","Prenume":"Laura","Varsta":26,"Salar":3900,"Departament":"Financiar","Senioritate":"junior"},{"CNP":"1950920879012","Nume":"Ilie","Prenume":"Gabriel","Varsta":36,"Salar":6500,"Departament":"Management","Senioritate":"senior"},{"CNP":"2981021980123","Nume":"Mihalache","Prenume":"Adina","Varsta":28,"Salar":4400,"Departament":"Marketing","Senioritate":"mid"},{"CNP":"1971122091234","Nume":"Sandu","Prenume":"Robert","Varsta":31,"Salar":5700,"Departament":"IT","Senioritate":"senior"},{"CNP":"2991223102345","Nume":"Lazar","Prenume":"Monica","Varsta":24,"Salar":3300,"Departament":"HR","Senioritate":"junior"}]
# persoane = []

#codul merge - scrie persoane in lista ca si dictionare
def adauga_persoane ():
    cnp = input("CNP :")
    nume = input("Nume : ")
    prenume = input("Prenume : ")
    varsta = int(input("Varsta : "))
    salariu = float(input("Salariu :"))
    departament = input("Departament :")
    senioritate = input("Senioritate (junior, mid, senior) : ")
    persoana = {
        "cnp": cnp,
        "nume": nume,
        "prenume": prenume,
        "varsta" : varsta,
        "salariu" : salariu,
        "departament" : departament,
        "senioritate" : senioritate
    }
    persoane.append(persoana)
    with open ('lista_angajati.json','w') as my_file :
        json.dump(persoane,my_file, indent = 4)

## codul merge - stie sa caute si sa afiseze persoana cautata            
def cauta_persoane (cauta):
    with open ('lista_angajati.json','r') as my_file :
        date = json.load(my_file)
    for elem in date :
        if elem['CNP'] == cauta :
            print(elem)
        else :
            print(f'Nu s-a gasit persoana cu CNP : {cauta}')
            break

# codul merge - stie sa modifice fiecare informatie al angajatului daca se doreste
def modificare_persoane (cauta):
    cauta = input("introdu cnp cautat pentru modificare")
    with open ('lista_angajati.json','r') as my_file :
        date = json.load(my_file)
    for elem in date : 
        if elem['CNP'] == cauta :
            while True : 
                optiune = input('Ce anume vrei sa modifici : Nume, Prenume, Varsta, Salar, Departament, Senioritate ? sau exit pentru iesire si salvare')
                if optiune == 'exit':
                    break
                if optiune.capitalize() == 'Nume':
                    var = input("Intordu noul nume : ")
                    elem['Nume'] = var.capitalize()
                if optiune.capitalize() == 'Prenume':
                    var = input("Intordu noul prenume : ")
                    elem['Prenume'] = var.capitalize()
                if optiune.capitalize() == 'Varsta':
                    while True : 
                        var = input("Intordu noua varsta : ")
                        if var.isdigit() :
                            elem['Varsta'] = int(var)
                            print('Varsta a fost modificata !') 
                            break                       
                        else :
                            print('Varsta trebuie sa fie formata din cifre')                            
                if optiune.capitalize() == 'Salar' :
                    while True :
                        var = float(input("Intordu noul salariu : "))
                        if var.isdigit() :
                            elem['Salar'] = var
                            print("Salariul a fost modificat !")
                            break
                        else :
                            print("Salariul trebuie sa fie format din cifre")
                if optiune.capitalize() == 'Departament':
                    var = input("Intordu noul departament : ")
                    elem['Departament'] = var.capitalize()
                if optiune.capitalize() == 'Senioritate':
                    var = input("Intordu noua senioritate : ")
                    elem['Senioritate'] = var.capitalize()
    with open ('lista_angajati.json','w') as my_file :
            json.dump(date,my_file, indent = 4)

def stergere_persoane(cauta):
    with open ('lista_angajati.json','r') as my_file :
        date = json.load(my_file)
    for elem in date : 
        if elem['CNP'] == cauta :
            elem.clear()
    with open ('lista_angajati.json','w') as my_file :
            json.dump(date,my_file, indent = 4)


while True :
    print(
    """
	1) Adaugare angajat
	2) Cautare angajat (dupa CNP)
	3) Modificare date angajat (dupa CNP)
	4) Stergere angajat (dupa CNP)
	5) Afisare angajati
	6) Calcul cost total salarii companie
	7) Calcul cost total salarii departament
	8) Calcul fluturas salar angajat (dupa CNP)
	9) Afisarea angajatilor pe baza senioritatii
	10) Afisarea angajatilor pe baza departamentului
	11) Iesire - apasa 0
    """
        ) 
    optiune = input("Alege optiune : ")
    if optiune == '0' :
        print("Ai iesit din sistem ! ")
        break
    if optiune == "1" :
        adauga_persoane()
    if optiune == "2" :
        cauta = input("Introdu cnp-ul cautat : ")
        if len(cauta) == 13 :
            cauta_persoane (cauta)
        else : 
            print(f'CNP-ul : {cauta} nu are toate cifrele')
    if optiune == "3" :
        cauta = input("Introdu cnp-ul persoanei unde vrei sa faci modificari : ")
        if len(int(cauta)) == 13 :
            modificare_persoane (cauta)
            print(f'''
                  Modificarile au fost salvate !
                  Acestea sunt noile date ale persoanei :
                  {cauta_persoane(cauta)}
                  ''')
        else : 
            print(f'CNP-ul : {cauta} nu are toate cifrele')
    if optiune == '4' :
        cauta = input("Intordu cnp-ul persoanei pe care vrei sa o stergi : ")
        stergere_persoane(cauta)
