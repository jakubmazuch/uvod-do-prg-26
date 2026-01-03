class Kocka:
    def __init__(self, jmeno, vek, vaha):
        self.jmeno = jmeno
        self.vek = vek
        self.vaha = vaha

    def prede(self):
        print(f"{self.jmeno} přede.")

    def snez(self, gramy):
        self.vaha += gramy * 0.01
