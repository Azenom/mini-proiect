import json, os, csv
from typing import List, Dict, Any

def functie_citire ():
    with open("lista_angajati.json", "r") as my_file:
        date = json.load(my_file)
    return date

def functie_scriere(param):
    with open("lista_angajati.json", "w") as my_file:
        json.dump(param, my_file, indent=4)

def validare_cnp(cnp: str) -> bool:
    """
    Verifica daca un CNP este valid:
    - contine doar cifre
    - are exact 13 caractere
    """
    if cnp.isdigit() and len(cnp) == 13 :
        return True
    else : 
        print("CNP invalid! Trebuie să aibă 13 cifre !!!")
        return False

def export_csv_filtrat(
    lista_angajati: List[Dict[str, Any]],camp_filtru: str,cauta: str,fisier_csv: str) -> None:
    """
    Filtrează angajații după valoarea unui câmp și exportă rezultatul într-un fișier CSV.

    Parametri:
        lista_angajati (List[Dict[str, Any]]):
            Lista de angajați, fiecare reprezentat ca dicționar.
        camp_filtru (str):
            Cheia din dicționar după care se face filtrarea.
        cauta (str):
            Valoarea căutată pentru filtrare (comparare case-insensitive).
        fisier_csv (str):
            Calea către fișierul CSV ce va fi generat.

    Returnează:
        None
    """
    os.makedirs(os.path.dirname(fisier_csv), exist_ok=True)
    # Filtrarea angajatilor
    lista_filtrata = [
        [elem['Nume'] + ' ' + elem['Prenume']] 
        for elem in lista_angajati 
        if str(elem[camp_filtru]).strip().lower() == cauta.lower()
                    ]
    # Scriere CSV
    with open(fisier_csv, 'w', newline='', encoding='utf-8') as my_file:
        writer = csv.writer(my_file)
        writer.writerow(["Nume Prenume", cauta])
        writer.writerows(lista_filtrata)
    if lista_filtrata:
        print(f"CSV-ul a fost generat: {os.path.abspath(fisier_csv)}")
    else:
        print(f"Nu s-au gasit angajati in {camp_filtru} : '{cauta}'")