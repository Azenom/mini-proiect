import json

def functie_citire ():
    with open("lista_angajati.json", "r") as my_file:
        data = json.load(my_file)
    return data

def functie_scriere(param):
    with open("lista_angajati.json", "w") as my_file:
        json.dump(param, my_file, indent=4)