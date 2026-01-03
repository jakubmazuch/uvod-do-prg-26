class BankovniUcet:
    def __init__(self, majitel, zustatek):
        self.majitel = majitel
        self.zustatek = zustatek

    def vklad(self, castka):
        if castka < 0:
            print("Nelze vložit zápornou částku.")
            return False
        self.zustatek += castka
        print(f"Vloženo {castka} Kč. Aktuální zůstatek: {self.zustatek} Kč.")
        return True

    def vyber(self, castka):
        if castka < 0:
            print("Nelze vybrat zápornou částku.")
            return False

        poplatek = 0
        if castka < 300:
            poplatek = 10
        castka = castka + poplatek

        if castka > self.zustatek:
            print(f"Na účtu není dost peněz. Aktuální zůstatek: {self.zustatek} Kč.")
            return False

        self.zustatek -= castka
        print(f"Vybráno {castka} Kč. Aktuální zůstatek: {self.zustatek} Kč.")
        return True

    def info(self):
        print(f"Účet patří: {self.majitel},\nZůstatek: {self.zustatek} Kč.")
