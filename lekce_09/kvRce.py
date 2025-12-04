import math


def nacti(text):
    while True:
        try:
            return float(input(text))
        except ValueError:
            print("Chyba: Zadejte prosím číslo!")


print(f"Řešení kvadratické rovnice ax²+bx+c=0\n")

a = nacti("Zadej a: ")
b = nacti("Zadej b: ")
c = nacti("Zadej c: ")

if a == 0:
    print(f"To není kvadratická rovnice.")
else:
    D = b**2 - 4*a*c

    if D < 0:
        print(f"Rovnice nemá reálné kořeny.")
    else:
        koreny = []
        x1 = (-b + math.sqrt(D)) / (2*a)
        koreny.append(x1)

        if D > 0:
            x2 = (-b - math.sqrt(D)) / (2*a)
            koreny.append(x2)

        print("Kořeny kvadratické rovnice:")
        i = 1
        for x in koreny:
            print(f"x{i} = {x}")
            i += 1
