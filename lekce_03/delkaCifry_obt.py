a = input("Zadej číslo: ")
if a[0] == "-":
    a = a[1:]

delka = len(a)
print(f"Číslo {a} má {delka} cifer.")
