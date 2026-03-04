import os,csv
from functii_ajutor.citire_scriere import functie_citire, functie_scriere, validare_cnp
from datetime import datetime
from typing import Optional, Dict, Union

def adauga_persoane() -> None:
    """
    Adaugă manual una sau mai multe persoane în lista de angajați.

    Funcționalitate:
        - Verifică existența fișierului `lista_angajati.json`.
        - Încarcă datele existente sau creează o listă nouă.
        - Validează unicitatea și corectitudinea CNP-ului.
        - Verifică:
            * vârsta minimă (>= 18 ani)
            * salariul minim (> 4050)
            * senioritatea (Junior, Mid, Senior)
        - Salvează lista actualizată în fișier JSON.
        - Permite adăugarea repetată de persoane până la oprirea utilizatorului.

    Returns:
        None
    """

    if os.path.exists("lista_angajati.json"):
        persoane: list[dict[str, str | int | float]] = functie_citire()
    else:
        persoane: list[dict[str, str | int | float]] = []

    lista_cnp: list[str] = []

    for cnp in persoane:
        lista_cnp.append(cnp['CNP'])

    flag: bool = True

    while flag:

        while True:
            var: str = input("CNP: ")
            if validare_cnp(var) and var not in lista_cnp:
                cnp: str = var
                lista_cnp.append(var)
                break
            elif var in lista_cnp:
                print('CNP-ul exista deja !')

        nume: str = input("Nume: ").capitalize()
        prenume: str = input("Prenume: ").capitalize()

        while True:
            try:
                varsta: int = int(input("Varsta: "))
                if varsta <= 17:
                    print('Varsta minima este 18 ani !')
                    continue
                if varsta > 117:
                    print("Felicitari ai intrat in cartea recordurilor pentru vechimea pe acest pamant !!! ")
                    continue
                break
            except ValueError:
                print("Varsta trebuie sa fie un numar!")

        while True:
            try:
                salariu: float = float(input("Salariu: "))
                if salariu <= 4050:
                    print("Salariul trebuie sa fie mai mare ca minimul pe economie (4050)")
                    continue
                break
            except ValueError:
                print("Salariu trebuie sa fie un numar!")

        departament: str = input("Departament: ").capitalize()

        while True:
            var: str = input("Senioritate (Junior, Mid, Senior): ").capitalize()
            if var == 'Junior' or var == 'Mid' or var == 'Senior':
                senioritate: str = var
                break
            else:
                print(f'Nu s-a gasit senioritatea {var} introdusa !')

        persoana: dict[str, str | int | float] = {
            "CNP": cnp,
            "Nume": nume,
            "Prenume": prenume,
            "Varsta": varsta,
            "Salariu": salariu,
            "Departament": departament,
            "Senioritate": senioritate
        }
        # Update dictionar in lista de persoane
        persoane.append(persoana)
        # Scriere in fisier
        functie_scriere(persoane)

        opt: str = input("Doresti sa mai adaugi persoane? Da / Nu: ").strip().lower()
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
            print(elem)
            return elem

    print(f'Nu s-a găsit persoana cu CNP: {cauta}')

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
    
    # Partea de căutare și modificare a unui angajat după CNP
    # cauta = input("Introdu CNP-ul angajatului pe care vrei sa-l modifici: ")

    for elem in date:
        if elem['CNP'] == cauta:
            while True:
                optiune = input('''
                Ce anume vrei sa modifici?
                                
CNP, Nume, Prenume, Varsta, Salariu, Departament, Senioritate 
            --- Exit pentru salvare si iesire: 
                                ''')
                # ---------------------- Exit ----------------------
                if optiune.lower() == 'exit':
                    break

                # ---------------------- CNP ----------------------
                elif optiune.upper() == "CNP":
                    while True:
                        var = input("Introdu noul CNP: ")
                        if validare_cnp(var) and var not in lista_cnp and elem['CNP'] != var:
                            elem['CNP'] = var
                            print("CNP modificat!")
                            break
                        elif elem['CNP'] == var :
                            print('Ai introdus acelasi CNP !')
                        elif var in lista_cnp :
                            print("CNP-ul este duplicat !")

                # ---------------------- Nume ----------------------
                elif optiune.capitalize() == 'Nume':
                    while True:
                        var = input("Introdu noul nume: ")
                        if var.isalpha():
                            elem['Nume'] = var.capitalize()
                            print("Nume modificat!")
                            break
                        else:
                            print("Numele trebuie sa contina doar litere.")

                # ---------------------- Prenume ----------------------
                elif optiune.capitalize() == 'Prenume':
                    while True:
                        var = input("Introdu noul prenume: ")
                        if var.isalpha():
                            elem['Prenume'] = var.capitalize()
                            print("Prenume modificat!")
                            break
                        else:
                            print("Prenumele trebuie sa contina doar litere.")

                # ---------------------- Varsta ----------------------
                elif optiune.capitalize() == 'Varsta':
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

                # ---------------------- Salariu ----------------------
                elif optiune.capitalize() == 'Salariu':
                    while True:
                        try:
                            var = float(input("Introdu noul salariu: "))
                            if var >= 4050:
                                elem['Salariu'] = var
                                print("Salariu modificat!")
                                break
                            else:
                                print("Salariul trebuie sa fie mai mare decât 4050.")
                        except ValueError:
                            print("Salariul trebuie sa fie un numar!")

                # ---------------------- Departament ----------------------
                elif optiune.capitalize() == 'Departament':
                    while True:
                        var = input("Introdu noul departament: ")
                        if var.isalpha():
                            elem['Departament'] = var.capitalize()
                            print("Departament modificat!")
                            break
                        else:
                            print("Departamentul trebuie sa contina doar litere.")

                # ---------------------- Senioritate ----------------------
                elif optiune.capitalize() == 'Senioritate':
                    while True:
                        var = input("Introdu noua senioritate: ")
                        if var.isalpha():
                            elem['Senioritate'] = var.capitalize()
                            print("Senioritate modificata!")
                            break
                        else:
                            print("Senioritatea trebuie sa contina doar litere.")
            break  # iesim din for dupa ce am gasit angajatul
    
    # Salvează lista de dictionare în JSON ----------------------
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
    flag = False
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
            flag = True
            break
        
    if flag :
        # sa scrie fisierul si specific in ce folder 
        path = 'fisiere_output/fluturas.csv'
        exista_fisier = os.path.exists(path) # boolean
        with open(path, 'a', newline='', encoding='utf-8') as my_file:
            writer = csv.writer(my_file)
            if not exista_fisier or os.path.getsize(path) == 0:     
                # scriu header-ul doar dacă fișierul nu există sau este gol
                writer.writerow(["Nume Prenume", "CNP", "Salariu Net", "Data Curenta"])
            writer.writerows(date)
        print(f'Verifica fisierul din {os.path.abspath(path)} pentru detalii!')
    else :
        print(f"Nu s-a gasit CNP-ul : {cauta}")
    