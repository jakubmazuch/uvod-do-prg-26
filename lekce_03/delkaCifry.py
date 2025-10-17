a = int(input("Zadej číslo: "))
b = abs(a)

if b < 10:
    print(f"Číslo {a} je jednociferné.")
elif b < 100:
    print(f"Číslo {a} je dvouciferné.")
elif b < 1000:
    print(f"Číslo {a} je tříciferné.")
elif b < 10000:
    print(f"Číslo {a} je čtyřciferné.")
else:
    print(f"Číslo {a} má hodně cifer.")
