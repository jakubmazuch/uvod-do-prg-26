from random import randint

a = int(input("Zadej dolní mez (a):"))
b = int(input("Zadej horní mez (b):"))

if a > b:
    a, b = b, a

nahodne = randint(a, b)
pokus = 0

while True:
    tip = int(input("Hádej číslo: "))
    pokus += 1

    if tip > nahodne:
        print("Myslím si menší číslo.")
    elif tip < nahodne:
        print("Myslím si větší číslo.")
    else:
        print(f"BINGO! Uhádl jsi moje číslo {nahodne} na {pokus}. pokus!")
        break
