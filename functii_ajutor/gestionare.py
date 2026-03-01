import os,csv
from functii_ajutor.citire_scriere import functie_citire, functie_scriere, validare_cnp
from datetime import datetime
from typing import Optional, Dict, Union

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