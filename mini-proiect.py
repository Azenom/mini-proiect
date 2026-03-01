import json,csv, os
from functii_ajutor.citire_scriere import functie_citire, functie_scriere, validare_cnp, export_csv_filtrat
from functii_ajutor.meniu_optiuni import functie_meniu
from datetime import datetime
from typing import Optional, Dict, Union
from gestionare import cauta_persoane, modificare_persoane, stergere_persoane, fluturas

# persoane = [{"CNP":"1960101123456","Nume":"Popescu","Prenume":"Andrei","Varsta":29,"Salariu":4500,"Departament":"IT","Senioritate":"mid"},{"CNP":"2950502234567","Nume":"Ionescu","Prenume":"Maria","Varsta":30,"Salariu":5200,"Departament":"HR","Senioritate":"senior"},{"CNP":"1980703345678","Nume":"Georgescu","Prenume":"Mihai","Varsta":27,"Salariu":4000,"Departament":"Marketing","Senioritate":"mid"},{"CNP":"6020814456789","Nume":"Dumitrescu","Prenume":"Elena","Varsta":24,"Salariu":4060,"Departament":"Financiar","Senioritate":"junior"},{"CNP":"1970905567890","Nume":"Popa","Prenume":"Alexandru","Varsta":33,"Salariu":6000,"Departament":"IT","Senioritate":"senior"},{"CNP":"2961016678901","Nume":"Stan","Prenume":"Ioana","Varsta":28,"Salariu":4700,"Departament":"Vanzari","Senioritate":"mid"},{"CNP":"1951127789012","Nume":"Marin","Prenume":"Cristian","Varsta":31,"Salariu":5500,"Departament":"Logistica","Senioritate":"senior"},{"CNP":"2971208890123","Nume":"Voicu","Prenume":"Alina","Varsta":26,"Salariu":4060,"Departament":"IT","Senioritate":"junior"},{"CNP":"1980112991234","Nume":"Morar","Prenume":"Daniel","Varsta":35,"Salariu":6200,"Departament":"Management","Senioritate":"senior"},{"CNP":"2990213102345","Nume":"Radu","Prenume":"Bianca","Varsta":23,"Salariu":4060,"Departament":"Marketing","Senioritate":"junior"},{"CNP":"1970314213456","Nume":"Barbu","Prenume":"Paul","Varsta":32,"Salariu":5800,"Departament":"Financiar","Senioritate":"senior"},{"CNP":"2960415324567","Nume":"Tudor","Prenume":"Raluca","Varsta":27,"Salariu":4200,"Departament":"HR","Senioritate":"mid"},{"CNP":"1980516435678","Nume":"Neagu","Prenume":"Vlad","Varsta":30,"Salariu":5100,"Departament":"IT","Senioritate":"mid"},{"CNP":"2990617546789","Nume":"Florea","Prenume":"Diana","Varsta":25,"Salariu":4060,"Departament":"Vanzari","Senioritate":"junior"},{"CNP":"1960718657890","Nume":"Preda","Prenume":"Sorin","Varsta":34,"Salariu":6100,"Departament":"Logistica","Senioritate":"senior"},{"CNP":"2970819768901","Nume":"Enache","Prenume":"Laura","Varsta":26,"Salariu":4060,"Departament":"Financiar","Senioritate":"junior"},{"CNP":"1950920879012","Nume":"Ilie","Prenume":"Gabriel","Varsta":36,"Salariu":6500,"Departament":"Management","Senioritate":"senior"},{"CNP":"2981021980123","Nume":"Mihalache","Prenume":"Adina","Varsta":28,"Salariu":4400,"Departament":"Marketing","Senioritate":"mid"},{"CNP":"1971122091234","Nume":"Sandu","Prenume":"Robert","Varsta":31,"Salariu":5700,"Departament":"IT","Senioritate":"senior"},{"CNP":"2991223102345","Nume":"Lazar","Prenume":"Monica","Varsta":24,"Salariu":4060,"Departament":"HR","Senioritate":"junior"}]
# persoane = []

def adauga_persoane() -> None:
    """
    Permite adăugarea manuală a unei persoane în lista de angajați.
    Verifică validitatea datelor (CNP, varsta, salariu, senioritate) și salvează lista actualizată în JSON.
    """
    # Verifica daca fisierul exista si daca da Încarcă lista existentă sau daca nu creează creaza o lista noua
    if os.path.exists("lista_angajati.json"):
        persoane = functie_citire()
    else:
        persoane = []
    flag = True
    while flag:
        # CNP ----------------------
        while True:
            cnp = input("CNP: ")
            if validare_cnp(cnp):
                break
            print("CNP invalid! Trebuie sa aiba exact 13 cifre și să fie doar numere.")
        # Nume și prenume ----------------------
        nume = input("Nume: ").capitalize()
        prenume = input("Prenume: ").capitalize()
        # Varsta ----------------------
        while True:
            try:
                varsta = int(input("Varsta: "))
                if varsta <= 18 :
                    print('Varsta minima este 18 ani !')
                    continue
                if varsta > 117:
                    print("Felicitari ai intrat in cartea recordurilor pentru vechimea pe acest pamant !!! ")
                    continue
                break
            except ValueError:
                print("Varsta trebuie sa fie un numar!")
        # Salariu cu minim ----------------------
        while True:
            try:
                salariu = float(input("Salariu: "))
                if salariu <= 4050:
                    print("Salariul trebuie sa fie mai mare ca minimul pe economie (4050)")
                    continue
                break
            except ValueError:
                print("Salariu trebuie sa fie un numar!")
        # Departament și senioritate ----------------------
        departament = input("Departament: ").capitalize()
        senioritate = input("Senioritate (Junior, Mid, Senior): ").capitalize()
        # Creează dictionarul persoana și îl adaugă în listă ----------------------
        persoana = {
            "CNP": cnp,
            "Nume": nume,
            "Prenume": prenume,
            "Varsta": varsta,
            "Salariu": salariu,
            "Departament": departament,
            "Senioritate": senioritate
        }
        persoane.append(persoana)
        # Salvează în JSON ----------------------
        functie_scriere(persoane)
        # Continuare daca se doreste ----------------------
        opt = input("Doresti sa mai adaugi persoane? Da / Nu: ").strip().lower()
        if opt == "nu":
            print("Datele au fost salvate, te vei intoarce la meniul principal!")
            flag = False
        
def cauta_persoane(cauta: str) -> Optional[Dict[str, Union[str,int,float]]]:
    """
    Cauta o persoana dupa CNP si returneaza dictionarul cu datele acesteia.
    """
    date = functie_citire()
    for elem in date:
        if elem['CNP'] == cauta:
            return print(elem) 
    print(f'Nu s-a găsit persoana cu CNP: {cauta}')
    return None
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
        else:
            print("CNP invalid! Trebuie să aibă 13 cifre.")

def modificare_persoane(cauta: str) -> None:
    """
    Permite modificarea datelor unei persoane identificate prin CNP.
    Salveaza automat modificarile in fisierul JSON.
    """
    date = functie_citire()
    # Incarc toate CNP-urile intr-o lista pentru verificare unicitate CNP
    lista_cnp = []
    for cnp in date :
        lista_cnp.append(cnp['CNP'])
    for elem in date : 
        if elem['CNP'] == cauta :
            while True : 
                optiune = input('''        Ce anume vrei sa modifici ?
            CNP, Nume, Prenume, Varsta, Salariu, Departament, Senioritate sau Exit pentru salvare si iesire : ''')
                if optiune.lower() == 'exit':
                    break
                if optiune.upper() == "CNP":
                    while True :
                        var = input('Introdu noul CNP : ')
                        if validare_cnp(var) and (var not in lista_cnp or var == elem['CNP']):
                            elem['CNP'] = var
                            print('CNP modificat !')
                            break
                        else :
                            print(f"CNP-ul : {elem['CNP']} exista ! ")
                if optiune.capitalize() == 'Nume':
                    while True :
                        var = input("Introdu noul nume : ")
                        if var.isalpha():
                            elem['Nume'] = var.capitalize()
                            print('Nume modificat !')
                            break
                        else :
                            print('Numele trebuie sa contina doar litere')
                if optiune.capitalize() == 'Prenume':
                    while True :
                        var = input("Introdu noul prenume : ")
                        if var.isalpha():
                            elem['Prenume'] = var.capitalize()
                            print('Prenume modificat !')
                            break
                        else :
                            print('Prenumele trebuie sa contina doar litere')
                if optiune.capitalize() == 'Varsta':
                    while True:
                        try:
                            var = int(input("Introdu noua varsta: "))
                            if var <= 18:
                                print("Varsta minima este 18 ani!")
                                continue
                            if var > 117:
                                print("Varsta introdusa este nerealista!")
                                continue
                            elem['Varsta'] = var
                            print("Varsta modificata!")
                            break
                        except ValueError:
                            print("Varsta trebuie sa fie un numar!")                          
                if optiune.capitalize() == 'Salariu' :
                    while True:
                        try:
                            var = float(input("Introdu noul salariu: "))
                            if var >= 4050:
                                elem['Salariu'] = var
                                print("Salariu modificat!")
                                break
                            else:
                                print("Salariul trebuie să fie mai mare decât 4050")
                        except ValueError:
                            print("Salariul trebuie sa fie un număr!")
                if optiune.capitalize() == 'Departament':
                    while True :    
                        var = input("Introdu noul departament : ")
                        if var.isalpha():
                            elem['Departament'] = var.capitalize()
                            print('Departament modificat !')
                            break
                        else :
                            print("Departamentul trebuie sa fie format din litere")
                if optiune.capitalize() == 'Senioritate':
                    while True :
                        var = input("Introdu noua senioritate : ")
                        if var.isalpha():   
                            elem['Senioritate'] = var.capitalize()
                            print('Senioritate modficata !')
                            break
                        else :
                            print('Senioritatea trebuie sa fie formata din litere')
    functie_scriere(date)
def modificare_persoane_wrapper() -> None:
    """
    Cere CNP-ul persoanei de modificat, validează și apelează modificare_persoane.
    Continuă până când se introduce un CNP valid.
    """
    while True:
        cnp: str = input("Introdu CNP-ul persoanei de modificat: ")
        if validare_cnp(cnp):
            modificare_persoane(cnp)
            break
        else:
            print("CNP invalid! Trebuie să aibă 13 cifre.")

def stergere_persoane(cauta: str) -> None:
    """
    Sterge o persoana din lista dupa CNP si afiseaza un mesaj de confirmare.
    """
    date = functie_citire()
    gasit = False
    # Creez o lista goala in care pun persoanele ce nu au cnp-ul cautat si astfel scriu un fisier tot, mai putin cel gasit
    date_noi = []
    for elem in date:
        if elem['CNP'] == cauta:
            print(f'Persoana {elem["Nume"]} {elem["Prenume"]} a fost stearsa!')
            gasit = True
        else:
            date_noi.append(elem)
    if not gasit:
        print(f'Nu s-a gasit persoana cu CNP: {cauta}')
    functie_scriere(date_noi)
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

def fluturas(cauta: str) -> None:
    """
    Genereaza fluturas salarial pentru o persoana, calculand salariul net si scriind intr-un CSV.
    Formula : Salariu Net = Salariu Brut - CAS (25%) - CASS (10%) - Impozit ( 10% din (Salariu Brut - CAS (25%) - CASS (10%) ) )
    """
    persoane = functie_citire()
    date = []
    for elem in persoane : 
        if elem['CNP']== cauta :
            # unesc nume si prenume intr-o singura variabila
            nume_prenume = elem['Nume'] + " " + elem["Prenume"]
            salariu = elem['Salariu']
            # calculez salariul net si apoi il converstc in str ca sa apara si cuvantul : ron la final
            salar = salariu - 0.25 * salariu - 0.1 * salariu - 0.1 * (salariu - 0.25 * salariu - 0.1 * salariu)
            salariu_net = str(salar) + " ron"
            # adaug si data la final de lista ce contine nume si prenume, cnp, salariul net, data curenta
            data_curenta = datetime.now().strftime('%H:%M %d-%m-%Y')
            date.append([nume_prenume, elem['CNP'], salariu_net, data_curenta])
    # specific in ce folder sa scrie fisierul
    path = 'fisiere_output/fluturas.csv'
    exista_fisier = os.path.exists(path) # boolean
    with open(path, 'a', newline='', encoding='utf-8') as my_file:
        writer = csv.writer(my_file)
        if not exista_fisier or os.path.getsize(path) == 0:     
            # scriu header-ul doar dacă fișierul nu există sau este gol
            writer.writerow(["Nume Prenume", "CNP", "Salariu Net", "Data Curenta"])
        writer.writerows(date)
    print(f'Verifica fisierul din {os.path.abspath(path)} pentru detalii!')
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
        else:
            print("CNP invalid! Trebuie să aibă 13 cifre.")

def seniori() -> None:
    """
    Creeaza CSV cu angajatii filtrati dupa senioritate.
    """
    date = functie_citire()
    cauta = input("Introdu senioritatea: ")
    export_csv_filtrat(date, 'Senioritate', cauta, 'fisiere_output/senioritate.csv')

def depart() -> None:
    """
    Creeaza CSV cu angajatii filtrati dupa departament.
    """
    date = functie_citire()
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