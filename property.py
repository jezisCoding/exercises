class Avto:
    _pKolies = "niekolko do pici"
    
    @property
    def pKolies(self):
        return self._pKolies

    @pKolies.setter
    def pKolies(self, p):
        self._pKolies = p

a = Avto()
a.pKolies = 6
print(a.pKolies)
