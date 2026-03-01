import json, os, csv

def functie_citire ():
    with open("lista_angajati.json", "r") as my_file:
        data = json.load(my_file)
    return data

def functie_scriere(param):
    with open("lista_angajati.json", "w") as my_file:
        json.dump(param, my_file, indent=4)

def validare_cnp(cnp: str) -> bool:
    """
    Verifica daca un CNP este valid:
    - contine doar cifre
    - are exact 13 caractere
    """
    return cnp.isdigit() and len(cnp) == 13

def export_csv_filtrat(lista_angajati, camp_filtru, cauta, fisier_csv):
    """
    Filtreaza angajatii dupa camp_filtru == valoare si exporta intr-un CSV.
    """
    os.makedirs(os.path.dirname(fisier_csv), exist_ok=True)
    # Filtrarea angajatilor
    lista_filtrata = [
        [angajat['Nume'] + ' ' + angajat['Prenume']] 
        for angajat in lista_angajati 
        if str(angajat[camp_filtru]).strip().lower() == cauta.lower()
                    ]
    # Scriere CSV
    with open(fisier_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Nume Prenume", cauta])
        writer.writerows(lista_filtrata)
    if lista_filtrata:
        print(f"CSV-ul a fost generat: {os.path.abspath(fisier_csv)}")
    else:
        print(f"Nu s-au gasit angajati cu {camp_filtru} = '{cauta}'")