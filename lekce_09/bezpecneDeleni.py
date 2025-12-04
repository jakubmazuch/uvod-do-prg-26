def bezpecneDeleni(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Chyba: Nulou nelze dělit.")
        return None
    except Exception:
        print("Chyba: Jiná chyba.")
        return None


try:
    a = float(input("Zadejte první číslo: "))
    b = float(input("Zadejte druhé číslo: "))

    vysledek = bezpecneDeleni(a, b)

    if vysledek is not None:
        print(f"{a}÷{b}={vysledek}")

except ValueError:
    print("Chyba: Zadejte číselné hodnoty.")
