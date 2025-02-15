#!/usr/bin/env python3

# Aufgabe: Erstellen Sie eine Klasse 'BankAccount', die ein einfaches Bankkonto repräsentiert.

# 1. Die Klasse soll die folgenden Attribute (Member-Variablen) haben:
#    - Inhaber: Der Name des Kontoinhabers (öffentlich).
#    - Kontonummer: Eine eindeutige Kontonummer (öffentlich).
#    - __kontostand: Der aktuelle Kontostand (nicht öffentlich).

# 2. Implementieren Sie die folgenden Methoden:
#    - __init__: Initialisiert den Kontoinhaber, die Kontonummer und den anfänglichen Kontostand.
#    - einzahlen: Erhöht den Kontostand um einen bestimmten Betrag.
#    - abheben: Verringert den Kontostand um einen bestimmten Betrag, wenn genügend Guthaben vorhanden ist.
#    - get_kontostand: Gibt den aktuellen Kontostand zurück.

# 3. Implementieren Sie außerdem eine Methode __str__, die eine benutzerfreundliche Darstellung des Kontos zurückgibt.

# Optional:
# - Erstellen Sie eine Methode, die Transaktionen protokolliert und eine Liste von Ein- und Auszahlungen ausgibt.

class BankAccount:
    def __init__(self, inhaber, kontonummer, start_kontostand):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.__kontostand = start_kontostand

    def __str__(self):
        return f"Der Kontostand von {self.inhaber} mit der Kontonummer {self.kontonummer} beträgt {self.__kontostand}"

    def einzahlen(self, betrag):
        self.__kontostand += betrag

    def abheben(self, betrag):
        if betrag > self.__kontostand:
            print("Fehler: Nicht genügend Guthaben!")
        else:
            self.__kontostand -= betrag

    def get_kontostand(self):
        return self.__kontostand

konto1 = BankAccount("Max Mustermann", "DE123456789", 100.50)
print(konto1)

konto1.einzahlen(2000)
konto1.abheben(333)
print(f"Kontostand nach Abhebungen: {konto1.get_kontostand():.2f}€")
