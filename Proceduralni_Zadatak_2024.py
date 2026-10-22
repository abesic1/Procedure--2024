"""
Online kupovina uz unosom podataka

Korisnik će trebati unijeti svoje osobne podatke i podatke o kreditnoj kartici kako bi simulirali online kupovinu.
Program će validirati unešene podatke, šifrirati broj kartice te prikazati korisniku sažetak unesenih podataka.
Definirat ćemo dvije funkcije, jednu za validaciju unosa i drugu za šifriranje broja kartice i koristit ćemo petlje 
za ponovni unos u slučaju neispravnog unosa te rječnik i listu za pohranu podataka :)

U zadatku je jedini nedostatak to da bi trebali dodat još unos e-pošte ili broja telefona

"""
# definiramo funkciju koja validira unešen cvv
def validiraj_cvv(cvv):
    if len(cvv) == 3 and cvv.isdigit():
        return True
    else:
        return False

#funkcija koja šifrira broj kartice
def sifriraj_karticu(broj_kartice):
    if len(broj_kartice) == 19 and broj_kartice.count('-') == 3:
        return f"XXXX-XXXX-XXXX-{broj_kartice[-4:]}"
    else:
        return None

#glavni dio programa je unos podataka
def unos():
    #unos osobnih podataka
    ime = input("Unesi svoje ime: ")
    prezime = input("Unesi svoje prezime: ")
    datum_rođ = input("Unesi datum rođenja (npr. 01.01.2001): ")
    adresa = input("Unesi adresu (Bez kučnog broja): ")
    kućni_broj = input("Unesi kućni broj: ")

    #unos podataka o kartici s validacijom
    while True:
        kartica = input("Unesi broj kreditne kartice (npr. 1234-5678-9012-3456): ")
        if len(kartica) == 19 and kartica.count('-') == 3:
            break
        else:
            print("Krivi format broja kartice. Pokušajte ponovno.")

    while True:
        datum_ist = input("Unesi datum isteka kartice (npr. 01/25): ")
        if len(datum_ist) == 5 and datum_ist[2] == '/':
            break
        else:
            print("Krivi format datuma isteka. Pokušajte ponovno.")

    while True:
        cvv_broj = input("Unesi CVV broj (npr. 123): ")
        if validiraj_cvv(cvv_broj):
            break
        else:
            print("Krivi CVV broj. Pokušajte ponovno.")

    sifriran_broj_kartice = sifriraj_karticu(kartica)
    if sifriran_broj_kartice:
        print(f"Šifriran broj kartice: {sifriran_broj_kartice}")
    else:
        print("Došlo je do greške pri šifriranju broja kartice.")

    #spremanje podataka u rječnik pa listu
    korisnik = {
        "Ime": ime,
        "Prezime": prezime,
        "Datum rođenja": datum_rođ,
        "Adresa": adresa,
        "Kućni broj": kućni_broj,
        "Šifriran broj kartice": sifriran_broj_kartice,
        "Datum isteka kartice": datum_ist,
        "CVV broj": cvv_broj
    }

    lista_korisnika = []
    lista_korisnika.append(korisnik)

    #Ispisujemo unesene podatke u čist tuple
    print("\nSažetak unesenih podataka:")
    for key, value in korisnik.items(): #items() - vrača listu koja sadrži tuple za svaku vrijednost ključa
        print(f"{key}: {value}")

#Ovdje pokrečemo glavnu definiranu funkciju
unos()