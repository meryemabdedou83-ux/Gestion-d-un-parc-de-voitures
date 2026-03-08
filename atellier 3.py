class Voiture:

    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

    def afficherInformations(self):
        print(self.matricule, self.marque, self.couleur)

class Parc:

    def __init__(self, id, adresse, capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.listeVoitures = []

    def entrerVoiture(self, voiture):

        if len(self.listeVoitures) < self.capacite:
             self.listeVoitures.append(voiture)
                print("Voiture entrée dans le parc")
        else:
                print("Parc plein")