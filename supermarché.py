# -*- coding: utf-8 -*-
"""
@author: Souhaila
"""

def fidelite():
    name = {'Elena Davis': {'age': 28, 'code': 234},
            'David Bouvier': {'age': 57, 'code': 569},
            'Richard Levain': {'age': 43, 'code': 820}}
    option = input("Avez-vous votre carte de fidelité ?\n")
    if option == 'oui':
        bar= int(input("entrez le code de votre carte: \n"))
        for key in name:
            if name[key]['code'] == bar:
                print("Merci", key)
    if option == 'non':
        print("Passez une bonne journée")
        return


items = {'pomme': {'prix': 2, 'stock': 1, 'barre': 1},
         'eau': {'prix': 1, 'stock': 12, 'barre': 2},
         'chocolat': {'prix': 4, 'stock': 5, 'barre': 3},
         'banane': {'prix': 3, 'stock': 10, 'barre': 4}}


somme = 0
prixTotal = 0
prix = []
produits = []
stock = []

while True:   
    code = int(input("entrez le code barre de votre produit:"))
    while True: #POur 1 Client
        for key in items:
            if items[key]['barre'] == code:
                if items[key]['stock'] == 0 :
                    print("Nous n'en avons plus en stock")
                else:
                    prixTotal += (items[key]['prix'])
                    prix.append(items[key]['prix'])
                    produits.append(key)
                    print(key)
                    print("prix : ", items[key]['prix'], "€")
                    print("stock : ", items[key]['stock'])
                    items[key]['stock'] -= 1
                    print("Sous Total: ", prixTotal, "€")
                print("...........................................")
        option = input("ça sera tout ? y/n \n")
        if option == 'y':
            for i in range(len(produits)):
                print(produits[i], prix[i], "€")
            print("Total : ", prixTotal, "€")
            print(".................................................")
            fidelite()
            break
        elif option == 'n':
            code = int(input("entrez le code barre de votre produit:"))
    clientSuivant = input("Client suivant ? y/n \n")
    if clientSuivant == 'y':
        print("Bonjour")
    elif clientSuivant == 'n':
        break
    
