#!/usr/bin/env python3

# Aufgabe: Programmieren Sie einen Taschenrechner mit ausgelagerten Funktionen.

# 1. Erstellen Sie für jede der Grundrechenarten (Addition, Subtraktion, Multiplikation, Division) eine separate Funktion.
#    - Jede Funktion sollte zwei Argumente (Zahlen) als Eingabe akzeptieren und das Ergebnis der Berechnung zurückgeben.
#    - Die Funktionen sollten klar benannt und gemäß PEP8 formatiert sein.

# 2. Implementieren Sie eine Hauptfunktion (main), die:
#    - Den Benutzer auffordert, zwei Zahlen einzugeben.
#    - Den Benutzer auffordert, die gewünschte Operation auszuwählen (Addition, Subtraktion, Multiplikation, Division).
#    - Die entsprechende Rechenfunktion aufruft und das Ergebnis ausgibt.
#    - Eine Fehlerbehandlung integriert, um ungültige Eingaben und Division durch Null zu vermeiden.

# 3. Stellen Sie sicher, dass Ihr Code PEP8-konform ist:
#    - Verwenden Sie vier Leerzeichen für Einrückungen.
#    - Fügen Sie Leerzeichen um Operatoren ein.
#    - Halten Sie Zeilenlängen unter 79 Zeichen.
#    - Schreiben Sie geeignete Kommentare und verwenden Sie docstrings für Funktionen.

# Beispielablauf:
# - Der Benutzer gibt die Zahlen 10 und 5 ein.
# - Der Benutzer wählt die Operation 'Multiplikation'.
# - Die Funktion zur Multiplikation wird aufgerufen und das Ergebnis (50) wird ausgegeben.

# Optional: 
# - Fügen Sie weitere Funktionen hinzu, wie z.B. Potenzierung oder Modulo.
# - Implementieren Sie eine Schleife, um mehrere Berechnungen hintereinander durchzuführen, bis der Benutzer das Programm beendet.

def add_numbers(num1, num2):
    return num1 + num2

def sub_numbers( num1, num2):
    return num1 - num2

def multi_numbers(num1, num2):
    return num1 * num2

def div_numbers(num1, num2):
    if num2 == 0:
      print("Keine Division durch NULL")
      return None
    return num1 / num2

def main():
    try:
        num1 = float(input("Zahl1"))
        num2 = float(input("Zahl2"))
    except ValueError:
        print("Geben sie gültige Zahlen ein")
        return

    #print("Operation?:")
    operation = input("Geben sie eine Operation ein: ")

    if operation == "+":
      result = add_numbers(num1, num2)
    if operation == "-":
      result = sub_numbers(num1, num2)
    if operation == "*":
      result = multi_numbers(num1, num2)
    if operation == "/":
      result = div_numbers(num1, num2)
    else:
      print("Ungültige Eingabe!")
      return
  
    if result is not None:
      print(F"Das Ergebnis ist: {result}")

if __name__ == "__main__":
    main()
