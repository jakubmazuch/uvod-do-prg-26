a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("Trojúhleník lze sestrojit")
else:
    print("Trojúhleník nelze sestrojit")
