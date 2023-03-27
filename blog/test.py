input = [{"car": "bmw", "value": 1}, {"car": "mg", "value": 2, }, {"car": "emv", "value": 3}]


def transform(input):
    adding_value = 0
    for dictio in input:
        if 'bmw' in dictio.values():
            adding_value += (dictio["value"])
        elif 'mg' in dictio.values():
            adding_value += (dictio["value"])
    return f"la valeur est {adding_value}"


class Dictionnaire:
    def __init__(self):
        with open("liste_mots.txt") as fic_texte:
            liste_de_mots = fic_texte.read()

        self.socle = set(liste_de_mots.split())

    def appartenance(self, mot):
        if mot in self.socle:
            print(f"le mot {mot} existe")


dico = Dictionnaire()

dico.appartenance("paris")
dico.appartenance("python")
dico.appartenance("zorglub")
