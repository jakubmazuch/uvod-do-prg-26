a = int(input("Zadej první hranici: "))
b = int(input("Zadej druhou hranici: "))
c = int(input("Zadej krok: "))

if c == 0:
    print("Chyba. Krok nemůže být nulový.")

else:
    for x in range(a, b + (1 if c > 0 else -1), c):
        print(x)
