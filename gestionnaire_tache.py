#=====================================
#GESTIONNAIRE DE TACHE
#=====================================

taches = []

nombre = int(input("Combien de tache voulez_vous enregistrer ?"))

for i in range(nombre):

    tache = input("Entrer une tache : ")

    taches.append(tache)

print()
print("------- MES TACHES -------")

for tache in taches:
    print("-", tache)

    fichier = open("taches.txt", "w")

for tache in taches:
    fichier.write(tache + "\n")

fichier.close()

print() 
print("Taches enregistrée dans taches.txt")