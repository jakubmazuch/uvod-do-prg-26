from banka import BankovniUcet

ucet = BankovniUcet("Karel", 20000)

ucet.vyber(500)
ucet.vyber(1230)
ucet.vyber(2444)
ucet.vyber(260)
ucet.vklad(400)
ucet.vyber(-50)

ucet.info()
