n = int(input("Zadej vstup: "))

if n < 0:
    print("Faktorial neni definovan pro zaporna cisla.")
else:
    faktorial = 1
    for i in range(1, n+1):
        faktorial *= i

    print(f"{n}! = {faktorial}")
