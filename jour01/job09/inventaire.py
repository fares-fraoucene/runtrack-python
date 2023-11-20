import string

nom="i9-14900k"
prix_unitaire = 676.66
quantité_en_stock= 20
inflation10 = prix_unitaire * 10 / 100
prix_post_infla = prix_unitaire + inflation10

print(f"Nom :{nom}, Prix : {prix_post_infla}€, Quantité{quantité_en_stock}.")
nb_produit_souhaité = input()

if  int(nb_produit_souhaité) <=  quantité_en_stock:
    quantité_en_stock = quantité_en_stock - int(nb_produit_souhaité)
    # (quantité_en_stock) -= int(nb_produit_souhaité) 
else:
    print("Désolé le produit et hors stock")

print(f"Nom :{nom}, Prix : {prix_unitaire}€, Quantité{quantité_en_stock}")