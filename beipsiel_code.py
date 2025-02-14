class Buch:

    def __init__(self, titel:str, author: str):
        self.titel = titel
        self.author = author
        self._status = "verfügbar"

    def ausleihen(self):
        if self._status == "verfügbar":
            self._status = "ausgeliehen"
            print(f"Das Buch {self.titel} wurde ausgeliehen.")
        else:
            print(f"Das Buch {self.titel} wurde bereits ausgeliehen!")

    def zurückgegeben(self):
        if self._status == "ausgeliehen":
            self._status = "verfügbar"
            print(f"Das Buch {self.titel} wurde zurückgegeben.")
        else:
            print(f"Das Buch {self.titel} ist bereits verfügbar.")

    def get_status(self) -> str:
        return self._status

class Bücherregal:

    def __init__(self):
        self._bücher = [] #privates Attribut, das eine Liste von Büchern speichert

    def buch_hinzufügen(self, buch: Buch):
        self._bücher.append(buch)
        print(f"Das Buch {buch.titel} wurde dem Regal hinzugefügt.")

    def buch_entfernen(self, buch: Buch):
        if buch in self._bücher:
            self._bücher.remove(buch)
            print(f"Das Buch {buch.titel} wurde aus dem Regal entfernt.")
        else:
            print(f"Das Buch {buch.titel} ist nicht im Regal.")

    def alle_bücher_anzeigen(self):
        if self._bücher:
            print("Bücher im Regal:")
            for buch in self._bücher:
                status = buch.get_status()
                print(f" - {buch.titel} von {buch.author} (Status: {status})")
        else:
            print("Das Bücherregeal ist leer.")
            