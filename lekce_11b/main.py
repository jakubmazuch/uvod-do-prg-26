from auto import Auto

skoda = Auto("Škoda", 0)
trabant = Auto("Trabant", 0)

skoda.zrychli(50)
trabant.zrychli(140)

skoda.info()
trabant.info()

skoda.zpomal(100)
trabant.zpomal(15)

skoda.info()
trabant.info()
