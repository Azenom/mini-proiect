import os, json
persoane = [{"CNP":"1960101123456","Nume":"Popescu","Prenume":"Andrei","Varsta":29,"Salar":4500,"Departament":"IT","Senioritate":"mid"},{"CNP":"2950502234567","Nume":"Ionescu","Prenume":"Maria","Varsta":30,"Salar":5200,"Departament":"HR","Senioritate":"senior"},{"CNP":"1980703345678","Nume":"Georgescu","Prenume":"Mihai","Varsta":27,"Salar":4000,"Departament":"Marketing","Senioritate":"mid"},{"CNP":"6020814456789","Nume":"Dumitrescu","Prenume":"Elena","Varsta":24,"Salar":3500,"Departament":"Financiar","Senioritate":"junior"},{"CNP":"1970905567890","Nume":"Popa","Prenume":"Alexandru","Varsta":33,"Salar":6000,"Departament":"IT","Senioritate":"senior"},{"CNP":"2961016678901","Nume":"Stan","Prenume":"Ioana","Varsta":28,"Salar":4700,"Departament":"Vanzari","Senioritate":"mid"},{"CNP":"1951127789012","Nume":"Marin","Prenume":"Cristian","Varsta":31,"Salar":5500,"Departament":"Logistica","Senioritate":"senior"},{"CNP":"2971208890123","Nume":"Voicu","Prenume":"Alina","Varsta":26,"Salar":3800,"Departament":"IT","Senioritate":"junior"},{"CNP":"1980112991234","Nume":"Morar","Prenume":"Daniel","Varsta":35,"Salar":6200,"Departament":"Management","Senioritate":"senior"},{"CNP":"2990213102345","Nume":"Radu","Prenume":"Bianca","Varsta":23,"Salar":3400,"Departament":"Marketing","Senioritate":"junior"},{"CNP":"1970314213456","Nume":"Barbu","Prenume":"Paul","Varsta":32,"Salar":5800,"Departament":"Financiar","Senioritate":"senior"},{"CNP":"2960415324567","Nume":"Tudor","Prenume":"Raluca","Varsta":27,"Salar":4200,"Departament":"HR","Senioritate":"mid"},{"CNP":"1980516435678","Nume":"Neagu","Prenume":"Vlad","Varsta":30,"Salar":5100,"Departament":"IT","Senioritate":"mid"},{"CNP":"2990617546789","Nume":"Florea","Prenume":"Diana","Varsta":25,"Salar":3600,"Departament":"Vanzari","Senioritate":"junior"},{"CNP":"1960718657890","Nume":"Preda","Prenume":"Sorin","Varsta":34,"Salar":6100,"Departament":"Logistica","Senioritate":"senior"},{"CNP":"2970819768901","Nume":"Enache","Prenume":"Laura","Varsta":26,"Salar":3900,"Departament":"Financiar","Senioritate":"junior"},{"CNP":"1950920879012","Nume":"Ilie","Prenume":"Gabriel","Varsta":36,"Salar":6500,"Departament":"Management","Senioritate":"senior"},{"CNP":"2981021980123","Nume":"Mihalache","Prenume":"Adina","Varsta":28,"Salar":4400,"Departament":"Marketing","Senioritate":"mid"},{"CNP":"1971122091234","Nume":"Sandu","Prenume":"Robert","Varsta":31,"Salar":5700,"Departament":"IT","Senioritate":"senior"},{"CNP":"2991223102345","Nume":"Lazar","Prenume":"Monica","Varsta":24,"Salar":3300,"Departament":"HR","Senioritate":"junior"}]
# persoane = []

#codul merge - verifica daca fisierul exista ca sa nu suprascriem apoi adauga/scrie persoane in lista ca si dictionare
def adauga_persoane ():
    # Încarcă lista existentă sau creează una nouă
    if os.path.exists("lista_angajati.json"):
        with open("lista_angajati.json", "r") as my_file:
            persoane = json.load(my_file)
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
        # Creează obiectul persoana și îl adaugă în listă ----------------------
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
        with open("lista_angajati.json", "w") as my_file:
            json.dump(persoane, my_file, indent=4)
        # Continuare ----------------------
        opt = input("Doresti sa mai adaugi persoane? Da / Nu: ").strip().lower()
        if opt == "nu":
            print("Datele au fost salvate, te vei intoarce la meniul principal!")
            flag = False

# codul merge - stie sa caute si sa afiseze persoana cautata            
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
    with open ('lista_angajati.json','r') as my_file :
        date = json.load(my_file)
    for elem in date : 
        if elem['CNP'] == cauta :
            while True : 
                optiune = input('''Ce anume vrei sa modifici ?
                                Nume, Prenume, Varsta, Salar, Departament, Senioritate sau Exit pentru salvare si iesire : ''')
                if optiune.lower() == 'exit':
                    break
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
    with open ('lista_angajati.json','w') as my_file :
            json.dump(date,my_file, indent = 4)

# codul merge - stie sa stearga persoana cu toate detaliile ei din dictionar si sa o si afiseze 
def stergere_persoane(cauta):
    with open ('lista_angajati.json','r') as my_file :
        date = json.load(my_file)
    for elem in date : 
        if elem['CNP'] == cauta :
            print(f'Persoana : {elem["Nume"]} {elem["Prenume"]} a fost stearsa !')
            elem.clear()
    with open ('lista_angajati.json','w') as my_file :
            json.dump(date,my_file, indent = 4)

def calcul_total():
    with open ('lista_angajati.json','r') as my_file :
        date = json.load(my_file)
    suma = 0
    for elem in date :
        suma += elem["Salar"]
    print(suma)

def calcul_dep():
    with open ('lista_angajati.json','r') as my_file :
        date = json.load(my_file)
    sal_dep={}
    for elem in date :
        dep = elem["Departament"]
        sal = elem["Salar"]
        if dep not in sal_dep:
            sal_dep[dep] = 0
        sal_dep[dep] += sal
    for dep, total in sal_dep.items():
        print(f'Departamentul : {dep} are {total} ron in salarii')
        
# print(
#     """
# 	1) Adaugare angajat
# 	2) Cautare angajat (dupa CNP)
# 	3) Modificare date angajat (dupa CNP)
# 	4) Stergere angajat (dupa CNP)
# 	5) Afisare angajati
# 	6) Calcul cost total salarii companie
# 	7) Calcul cost total salarii departament
# 	8) Calcul fluturas salar angajat (dupa CNP)
# 	9) Afisarea angajatilor pe baza senioritatii
# 	10) Afisarea angajatilor pe baza departamentului
# 	11) Iesire - apasa 0
#     """
#         ) 
while True :
    optiune = input("Alege optiune : ")
    if optiune == '0' :
        print("Ai iesit din sistem ! ")
        break
    if optiune == "1" :           
        adauga_persoane()
    if optiune == "2" :
        while True :
            cauta = input("Introdu cnp-ul cautat : ")
            if len(cauta) == 13 :
                cauta_persoane (cauta)
                break
            else : 
                print(f'CNP-ul : {cauta} nu are toate cifrele')
    if optiune == "3" :
        cauta = input("Introdu cnp-ul persoanei unde vrei sa faci modificari : ")
        if len(cauta) == 13 :
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
    if optiune == '5' :
        with open ('lista_angajati.json','r') as my_file :
            date = json.load(my_file)
            print(json.dumps(date, indent=4))
    if optiune == '6' :
        print('Calcul cost total salarii companie : ',calcul_total())
    if optiune == '7' :        
        calcul_dep()
        