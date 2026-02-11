class Bancomat:
    def __init__(self, sold_init):
        self.sold = sold_init

    def depunere(self, suma):
        self.sold += suma
        return self.sold

    def retragere(self, suma):
        if self.sold > suma:
            self.sold -= suma
        else:
            print("Eroare, sold insuficient!")
    def afiseaza_sold(self):

        print(self.sold)

banc_sold = Bancomat(1000)
# Apeleaza functia de depunere si depune suma de 3000.
banc_sold.depunere(3000)
# Apeleaza iar functia de depunere, sa ajungi la un total de 10000
banc_sold.depunere(6000)
# Apeleaza functia de retragere, si retrage 4000.
banc_sold.retragere(4000)
# Apeleaza iar functia de retragere, retrage prea mult sa afisam mesajul de eroare.
banc_sold.retragere(10000)
# Afiseaza soldul curent.
banc_sold.afiseaza_sold()