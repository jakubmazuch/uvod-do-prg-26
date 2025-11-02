a = int(input("Zadej první hranici: "))
b = int(input("Zadej druhou hranici: "))
c = int(input("Zadej krok: "))

if c > 0:
    while a <= b:
        print(a)
        a += c
elif c == 0:
    print("Chyba.")
else:
    while a >= b:
        print(a)
        a += c
