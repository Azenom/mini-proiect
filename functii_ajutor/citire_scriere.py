import json, os, csv

def functie_citire ():
    with open("lista_angajati.json", "r") as my_file:
        data = json.load(my_file)
    return data

def functie_scriere(param):
    with open("lista_angajati.json", "w") as my_file:
        json.dump(param, my_file, indent=4)

def functie_scriere_csv(lista,path,cauta):
    exista_fisier = os.path.exists(path) # boolean
    with open(path, 'w', newline='', encoding='utf-8') as my_file:
        writer = csv.writer(my_file)
        if not exista_fisier or os.path.getsize(path) == 0:     
            # scriu header-ul doar dacă fișierul nu există sau este gol
            writer.writerow(["Nume Prenume", cauta.capitalize()])
        for elem in lista :
            writer.writerow([elem])
    print(f'Verifica fisierul din {os.path.abspath(path)} pentru detalii!')