x = int(input("Zadej celé číslo: "))

if x <= 1:
    print(f"Číslo {x} není prvočíslo.")
else:
    jePrvocislo = True
    i = 2
    delitele = []
    while i*i <= x:
        if x % i == 0:
            jePrvocislo = False
            delitele.append(i)
            druhy = x // i
            if druhy != i:
                delitele.append(druhy)
        i += 1

    if jePrvocislo:
        print(f"Číslo {x} je prvočíslo.")
    else:
        print(f"Číslo {x} není prvočíslo.")
        delitele.sort()
        print(f"Jeho dělitelé jsou: {delitele}")
