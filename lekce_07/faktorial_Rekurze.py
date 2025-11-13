def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n-1)

n = int(input("Zadej číslo: "))
if n < 0:
    print("Faktorial neni definovan pro zaporna cisla.")
else:
    print(f"{n}! = {faktorial(n)}")