a = int(input("Zadej první číslo: "))
b = int(input("Zadej další číslo: "))
c = int(input("Zadej poslední číslo: "))

max = float('-inf')
min = float('inf')

if a > max:
    max = a
if a < min:
    min = a

if b > max:
    max = b
if b < min:
    min = b

if c > max:
    max = c
if c < min:
    min = c

print(f"Největší číslo je {max}")
print(f"Nejmenší číslo je {min}")
