castka = int(input("Zadejte částku: "))

p5000 = castka // 5000
castka = castka % 5000

p2000 = castka // 2000
castka = castka % 2000

p1000 = castka // 1000
castka = castka % 1000

p500 = castka // 500
castka = castka % 500

p200 = castka // 200
castka = castka % 200

p100 = castka // 100
castka = castka % 100

p50 = castka // 50
castka = castka % 50

p20 = castka // 20
castka = castka % 20

p10 = castka // 10
castka = castka % 10

p5 = castka // 5
castka = castka % 5

p2 = castka // 2
castka = castka % 2

p1 = castka // 1
castka = castka % 1

print("5000 Kč:", p5000)
print("2000 Kč:", p2000)
print("1000 Kč:", p1000)
print("500 Kč:", p500)
print("200 Kč:", p200)
print("100 Kč:", p100)
print("50 Kč:", p50)
print("20 Kč:", p20)
print("10 Kč:", p10)
print("5 Kč:", p5)
print("2 Kč:", p2)
print("1 Kč:", p1)
