class Car():
    def __init__(self, cuntry, year, Gas, Vgas):
        self.cuntry = cuntry
        self.year = year
        self.Gas = Gas
        self.Vgas = Vgas

    def zapravka(self):
        int(self.Vgas)
        int(self.Gas)
        if self.Vgas > self.Gas:
            self.Gas += 10
            print('В баке', self.Gas, ' литров, а обём', self.Vgas, ' и можно заправлять')
        else:
            print('Обём бака', self.Vgas, ' а хотите налить ещё, когда там', self.Gas, 'литров и он переполнен')


Pogani_Huyara = Car('Moskva', '50 веков', 100, 50)
print(Pogani_Huyara.cuntry)
print(Pogani_Huyara.year)
Pogani_Huyara.zapravka()
