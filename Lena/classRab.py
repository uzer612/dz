class Rab:
    def __init__(self, how_many_char, char):
        self.how_many_char = how_many_char
        self.char = char
    def add(self, list):
        list2 = list.copy()
        if len(list2) < self.how_many_char:
            while len(list2) < self.how_many_char:
                list2.append(self.char)
        print(list2)
        return list2
    def clean(self, list):
        list2 = list[0:self.how_many_char]
        print(list2)
        return list2


listik = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

rab1 = Rab(5, 3)
rab1.add(listik)
rab1.clean(listik)

rab2 = Rab(13, 7)
rab2.add(listik)
rab2.clean(listik)

print('listik', listik)