binarniCislo = input("Zadej binární číslo: ")

platnyVstup = True
for znak in binarniCislo:
    if znak not in ["0", "1"]:
        platnyVstup = False
        break

if not platnyVstup or len(binarniCislo) == 0:
    print("Chybný vstup")
else:
    desitkove = 0
    for znak in binarniCislo:
        desitkove = desitkove * 2 + int(znak)

    print(f"BIN({binarniCislo}) = DEC({desitkove})")
