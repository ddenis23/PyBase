import random


class GhicesteNumarul:
    def __init__(self):
        self.numar_secret = random.randint(1, 100)

    def joaca(self):
        ghicit = False

        while not ghicit:
            try:
                numar = int(input("Introdu un număr între 1 și 100: "))

                if numar > self.numar_secret:
                    print("Prea mare! Încearcă din nou.")
                elif numar < self.numar_secret:
                    print("Prea mic! Încearcă din nou.")
                else:
                    print("Felicitări! Ai ghicit numărul.")
                    ghicit = True
            except ValueError:
                print("Te rog introdu un număr valid!")

    def joaca_din_nou(self):
        while True:
            self.joaca()
            raspuns = input("Vrei să joci din nou? (da/nu): ").lower()

            if raspuns != "da":
                print("Mulțumesc pentru joc! 👋")
                break
            self.numar_secret = random.randint(1, 100)

joc = GhicesteNumarul()
joc.joaca_din_nou()
