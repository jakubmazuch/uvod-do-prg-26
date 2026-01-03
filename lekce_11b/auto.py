class Auto:
    def __init__(self, znacka, rychlost):
        self.znacka = znacka
        self.rychlost = rychlost

    def zrychli(self, delta):
        self.rychlost += delta

    def zpomal(self, delta):
        self.rychlost -= delta
        if self.rychlost < 0:
            self.rychlost = 0

    def info(self):
        print(f"Auto {self.znacka} jede rychlostí {self.rychlost} km/h.")
