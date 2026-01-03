class Student:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.znamky = []

    def pridej_znamku(self, z):
        self.znamky.append(z)

    def prumer(self):
        if len(self.znamky) == 0:
            return None
        return sum(self.znamky) / len(self.znamky)

    def info(self):
        pr = self.prumer()
        if pr is None:
            print(f"Student {self.jmeno} zatím nemá žádné známky.")
        else:
            print(f"Student {self.jmeno} má průměr {pr:.2f}.")
