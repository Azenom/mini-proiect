import os, json, csv 
from functii_ajutor.citire_scriere import functie_citire, functie_scriere, functie_scriere_csv
from functii_ajutor.meniu_optiuni import functie_meniu
from datetime import datetime

persoane = [{"CNP":"1960101123456","Nume":"Popescu","Prenume":"Andrei","Varsta":29,"Salar":4500,"Departament":"IT","Senioritate":"mid"},{"CNP":"2950502234567","Nume":"Ionescu","Prenume":"Maria","Varsta":30,"Salar":5200,"Departament":"HR","Senioritate":"senior"},{"CNP":"1980703345678","Nume":"Georgescu","Prenume":"Mihai","Varsta":27,"Salar":4000,"Departament":"Marketing","Senioritate":"mid"},{"CNP":"6020814456789","Nume":"Dumitrescu","Prenume":"Elena","Varsta":24,"Salar":3500,"Departament":"Financiar","Senioritate":"junior"},{"CNP":"1970905567890","Nume":"Popa","Prenume":"Alexandru","Varsta":33,"Salar":6000,"Departament":"IT","Senioritate":"senior"},{"CNP":"2961016678901","Nume":"Stan","Prenume":"Ioana","Varsta":28,"Salar":4700,"Departament":"Vanzari","Senioritate":"mid"},{"CNP":"1951127789012","Nume":"Marin","Prenume":"Cristian","Varsta":31,"Salar":5500,"Departament":"Logistica","Senioritate":"senior"},{"CNP":"2971208890123","Nume":"Voicu","Prenume":"Alina","Varsta":26,"Salar":3800,"Departament":"IT","Senioritate":"junior"},{"CNP":"1980112991234","Nume":"Morar","Prenume":"Daniel","Varsta":35,"Salar":6200,"Departament":"Management","Senioritate":"senior"},{"CNP":"2990213102345","Nume":"Radu","Prenume":"Bianca","Varsta":23,"Salar":3400,"Departament":"Marketing","Senioritate":"junior"},{"CNP":"1970314213456","Nume":"Barbu","Prenume":"Paul","Varsta":32,"Salar":5800,"Departament":"Financiar","Senioritate":"senior"},{"CNP":"2960415324567","Nume":"Tudor","Prenume":"Raluca","Varsta":27,"Salar":4200,"Departament":"HR","Senioritate":"mid"},{"CNP":"1980516435678","Nume":"Neagu","Prenume":"Vlad","Varsta":30,"Salar":5100,"Departament":"IT","Senioritate":"mid"},{"CNP":"2990617546789","Nume":"Florea","Prenume":"Diana","Varsta":25,"Salar":3600,"Departament":"Vanzari","Senioritate":"junior"},{"CNP":"1960718657890","Nume":"Preda","Prenume":"Sorin","Varsta":34,"Salar":6100,"Departament":"Logistica","Senioritate":"senior"},{"CNP":"2970819768901","Nume":"Enache","Prenume":"Laura","Varsta":26,"Salar":3900,"Departament":"Financiar","Senioritate":"junior"},{"CNP":"1950920879012","Nume":"Ilie","Prenume":"Gabriel","Varsta":36,"Salar":6500,"Departament":"Management","Senioritate":"senior"},{"CNP":"2981021980123","Nume":"Mihalache","Prenume":"Adina","Varsta":28,"Salar":4400,"Departament":"Marketing","Senioritate":"mid"},{"CNP":"1971122091234","Nume":"Sandu","Prenume":"Robert","Varsta":31,"Salar":5700,"Departament":"IT","Senioritate":"senior"},{"CNP":"2991223102345","Nume":"Lazar","Prenume":"Monica","Varsta":24,"Salar":3300,"Departament":"HR","Senioritate":"junior"}]
# persoane = []

# codul merge - verifica daca fisierul exista ca sa nu suprascriem apoi adauga/scrie persoane in lista ca si dictionare
def adauga_persoane ():
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
            if cnp.isdigit() and len(cnp) == 13:
                break
            print("CNP invalid! Trebuie sa aiba exact 13 cifre și să fie doar numere.")
        # Nume și prenume ----------------------
        nume = input("Nume: ").capitalize()
        prenume = input("Prenume: ").capitalize()
        # Varsta ----------------------
        while True:
            try:
                varsta = int(input("Varsta: "))
                break
            except ValueError:
                print("Varsta trebuie sa fie un numar!")
        # Salariu cu minim ----------------------
        while True:
            try:
                salariu = float(input("Salariu: "))
                if salariu < 4050:
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

# codul merge - stie sa caute si sa afiseze persoana cautata            
# def cauta_persoane (cauta):
cauta = input('introdu cnp : ')
date = functie_citire()
counter = 0
for elem in date :
    if elem['CNP'] == cauta :
        print(elem)
        break
    else : counter +=1

if counter > 0 :
    print(f'Nu s-a gasit persoana cu CNP : {cauta}')
        


# codul merge - stie sa modifice fiecare informatie al angajatului daca se doreste
def modificare_persoane (cauta):
    lista_cnp = []
    date = functie_citire()
    for elem in date : 
        if elem['CNP'] == cauta :
            while True : 
                optiune = input('''        Ce anume vrei sa modifici ?
            CNP, Nume, Prenume, Varsta, Salar, Departament, Senioritate sau Exit pentru salvare si iesire : ''')
                if optiune.lower() == 'exit':
                    break
                if optiune.upper() == "CNP":
                    while True :
                        for cnp in date :
                            lista_cnp.append(cnp['CNP'])
                        var = input('Introdu noul CNP : ')
                        if var.isdigit() and var not in lista_cnp :
                            elem['CNP'] = var
                            print('CNP modificat !')
                            break
                        else :
                            print(f'CNP=ul : {elem['CNP']} exista ! ')
                if optiune.capitalize() == 'Nume':
                    while True :
                        var = input("Intordu noul nume : ")
                        if var.isalpha():
                            elem['Nume'] = var.capitalize()
                            print('Nume modificat !')
                            break
                        else :
                            print('Numele trebuie sa contina doar litere')
                if optiune.capitalize() == 'Prenume':
                    while True :
                        var = input("Intordu noul prenume : ")
                        if var.isalpha():
                            elem['Prenume'] = var.capitalize()
                            print('Prenume modificat !')
                            break
                        else :
                            print('Prenumele trebuie sa contina doar litere')
                if optiune.capitalize() == 'Varsta':
                    while True : 
                        var = input("Intordu noua varsta : ")
                        if var.isdigit() :
                            elem['Varsta'] = int(var)
                            print('Varsta modificata !') 
                            break                       
                        else :
                            print('Varsta trebuie sa fie formata din cifre')                            
                if optiune.capitalize() == 'Salar' :
                    while True :
                        var = float(input("Intordu noul salariu : "))
                        if var.isdigit() :
                            elem['Salar'] = var
                            print("Salariul modificat !")
                            break
                        else :
                            print("Salariul trebuie sa fie format din cifre")
                if optiune.capitalize() == 'Departament':
                    while True :    
                        var = input("Intordu noul departament : ")
                        if var.isalpha():
                            elem['Departament'] = var.capitalize()
                            print('Departament modificat !')
                            break
                        else :
                            print("Departamentul trebuie sa fie format din litere")
                if optiune.capitalize() == 'Senioritate':
                    while True :
                        var = input("Intordu noua senioritate : ")
                        if var.isalpha():   
                            elem['Senioritate'] = var.capitalize()
                            print('Senioritate modficata !')
                        else :
                            print('Senioritatea trebuie sa fie formata din litere')
    functie_scriere(date)

# codul merge - stie sa stearga persoana cu toate detaliile ei din dictionar si sa o si afiseze 
def stergere_persoane(cauta):
    date = functie_citire()
    for elem in date : 
        if elem['CNP'] == cauta :
            print(f'Persoana : {elem["Nume"]} {elem["Prenume"]} a fost stearsa !')
            elem.clear()
    functie_scriere(date)

# codul merge - stie sa calculeze totaul de salarii din companie
def calcul_total():
    date = functie_citire()
    suma = 0
    for elem in date :
        suma += elem["Salar"]
    print(suma)

# codul merge - stie sa calculeze si sa afiseze salariile totale pe departament
def calcul_dep():
    date = functie_citire()
    sal_dep={}
    for elem in date :
        dep = elem["Departament"]
        sal = elem["Salar"]
        if dep not in sal_dep:
            sal_dep[dep] = 0
        sal_dep[dep] += sal
    for dep, total in sal_dep.items():
        print(f'Departamentul : {dep} are {total} ron in salarii')

# codul merge - stie sa calculeze salariul net si sa faca o lista cu nume+prenume, cnp, salariul net, data curenta
# Formula : Salariu Net = Salariu Brut - CAS (25%) - CASS (10%) - Impozit ( 10% din (Salariu Brut - CAS (25%) - CASS (10%) ) )
def fluturas (cauta):
    persoane = functie_citire()
    date = []
    for elem in persoane : 
        if elem['CNP']== cauta :
            # unesc nume si prenume intr-o singura variabila
            nume_prenume = elem['Nume'] + " " + elem["Prenume"]
            salariu = elem['Salar']
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

# codul merge - stie sa citeasca detele la zi si sa suprascrie in csv la fiecare interogare de senioritate
def seniori ():
    date = functie_citire()
    # extragem senioritățile unice și le transformăm în lowercase
    lista_seni = {elem['Senioritate'].lower() for elem in date}
    lista=[]
    while True:
        cauta = input('Introdu senioritatea: ').lower()
        if cauta in lista_seni:
            for elem in date:
                if elem['Senioritate'].lower() == cauta:
                    nume_prenume = elem['Nume']+ ' ' + elem['Prenume']
                    lista.append(nume_prenume)
            break
        else:
            print(f'Nu exista {cauta}. Reintrodu : ')
    path = 'fisiere_output/senioritate.csv'
    functie_scriere_csv(lista,path,cauta)

# codul merge - stie sa citeasca detele la zi si sa suprascrie in csv la fiecare interogare de departament
def depart () :
    date = functie_citire()
    departamente = list({elem["Departament"] for elem in date})
    print(departamente)
    lista = []
    cauta = input("Introdu departamentul cautat : ")
    for dep in departamente :
        if cauta.capitalize() == dep or ( len(cauta)<3 and dep == cauta.upper() ) or dep == cauta:
            for elem in date :
                if elem["Departament"] == dep:
                    nume_prenume = elem['Nume']+ ' ' + elem['Prenume']
                    lista.append(nume_prenume)

    path = 'fisiere_output/departament.csv'
    functie_scriere_csv(lista,path,cauta)

# Meniul principal ------------------------------------------------------
# functie_meniu()
# while True :
#     optiune = input("Alege optiune : ")
#     if optiune == '0' :
#         print("Ai iesit din sistem ! ")
#         break
#     if optiune == "1" :           
#         adauga_persoane()
#     if optiune == "2" :
#         while True :
#             cauta = input("Introdu cnp-ul cautat : ")
#             if len(cauta) == 13 :
#                 cauta_persoane (cauta)
#                 break
#             else : 
#                 print(f'CNP-ul : {cauta} nu are toate cifrele')
#     if optiune == "3" :
#         cauta = input("Introdu cnp-ul persoanei unde vrei sa faci modificari : ")
#         if len(cauta) == 13 :
#             temp = cauta_persoane(cauta)
#             print(temp)
#             modificare_persoane (cauta)
#             print(f'''
#                   Modificarile au fost salvate !
#                   Acestea sunt noile date ale persoanei :
#                   {temp}
#                   ''')
#         else : 
#             print(f'CNP-ul : {cauta} nu are toate cifrele')
#     if optiune == '4' :
#         cauta = input("Intordu cnp-ul persoanei pe care vrei sa o stergi : ")
#         stergere_persoane(cauta)
#     if optiune == '5' :
#         date = functie_citire()
#         print(json.dumps(date, indent=4))
#     if optiune == '6' :
#         print('Calcul cost total salarii companie : ',calcul_total())
#     if optiune == '7' :        
#         calcul_dep()
#     if optiune == '8' :
#         while True :
#             cauta = input("Introdu cnp-ul cautat : ")
#             if len(cauta) == 13 :
#                 fluturas (cauta)
#                 break
#             else : 
#                 print(f'CNP-ul : {cauta} nu are toate cifrele')
#     if optiune == '9' :
#         seniori()
#     if optiune == '10':
#         depart()
                


