a = int(input("Zadej dolní hranici: "))
b = int(input("Zadej horní hranici: "))
c = int(input("Zadej krok: "))

if c == 0:
    print("Chyba. Krok nemůže být nulový.")

else:
    if c > 0:
        for x in range(a, b+1, c):
            print(x)
    else:
        for x in range(a, b-1, c):
            print(x)
