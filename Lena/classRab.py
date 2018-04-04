class Rab:
    def __init__(self, how_many_char, char):
        self.list_of_number = []
        self.resultat_clean = []
        self.resultat_add = []
    def add(self, how_many_char, char):
        for i in range(how_many_char):
            resultat_add = self.list_of_number.append(char)
    def clean(self, how_many_char, char):
        while num_of_elenemt > how_many_char:
            resultat_clean = del self.list_of_number[num_of_elenemt]
            num_of_elenemt--
        print(resultat_clean)

rab1 = Rab()
rab1.add(5, 3)
