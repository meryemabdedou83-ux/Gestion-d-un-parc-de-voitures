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

def sortirVoiture(self, voiture):

    if voiture in self.listeVoitures:
        self.listeVoitures.remove(voiture)
        print("Voiture sortie du parc")
    else:
        print("Voiture non trouvée")

def calculerNbrPlacesLibres(self):
    return self.capacite - len(self.listeVoitures)

from voiture import Voiture
from parc import Parc

parc = Parc(1, "Ottawa", 3)

v1 = Voiture("111", "Toyota", "Rouge")
v2 = Voiture("222", "Honda", "Noir")

parc.entrerVoiture(v1)
parc.entrerVoiture(v2)

parc.sortirVoiture(v1)

print("Places libres:", parc.calculerNbrPlacesLibres())

# Création
voiture1 = Voiture("Toyota", "Corolla", 2020, "ABC123")
voiture2 = Voiture("audi", "RS3", 2019, "XYZ789")
voiture3 = Voiture("bmw", "noir", 2021, "LMN456")

parc_voitures.append(voiture1)
parc_voitures.append(voiture2)
parc_voitures.append(voiture3)

print("Voitures dans le parc :")
for v in parc_voitures:
    print(v)


def sortir_voiture(immatriculation):
    for voiture in parc_voitures:
        if voiture.immatriculation == immatriculation:
                parc_voitures.remove(voiture)
                print(f"La voiture {voiture} est sortie du parc.")
                return
    print("Voiture non trouvée dans le parc.")


sortir_voiture("XYZ789")

print("\nParc après sortie :")
    for v in parc_voitures:
        print(v)