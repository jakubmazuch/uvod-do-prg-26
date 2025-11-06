def bankomat(castka):
    bankovky = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    vysledek = {}
    
    for i in bankovky:
        pocet = castka // i
        castka %= i
        vysledek[i] = pocet
        
    return vysledek

#main
castka = int(input("Zadej částku:"))
vysledek = bankomat(castka)

#vypis
for i, pocet in vysledek.items():
    if pocet > 0:
        print(f"{i} Kč: {pocet}×")