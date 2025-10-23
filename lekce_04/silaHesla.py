heslo = input("Zadej heslo: ")

if len(heslo) >= 8 and ("@" in heslo or "#" in heslo):
    print("Heslo je dostatečně silně")
else:
    print("Heslo je slabé")
