import json, os, csv

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

def export_csv_filtrat(lista_angajati, camp_filtru, cauta, fisier_csv):
    """
    Filtreaza angajatii dupa camp_filtru == valoare si exporta intr-un CSV.
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