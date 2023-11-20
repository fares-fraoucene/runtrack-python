montant_initial_de_linvestissement = 5000
taux_de_rendement_annuel = 1
gain = montant_initial_de_linvestissement * taux_de_rendement_annuel / 100
montant_final = montant_initial_de_linvestissement + gain
print(f"Gain: {gain}€, Montant final: {montant_final}€, Taux de rendement annuel: {taux_de_rendement_annuel}%.")

montant_final += 5000
taux_de_rendement_annuel += 2
gain = montant_final * taux_de_rendement_annuel / 100
montant_final += gain
print(f"Gain: {gain}€, Montant final: {montant_final}€, Taux de rendement annuel: {taux_de_rendement_annuel}%.")

montant_final -= montant_final * 10 / 100
taux_de_rendement_annuel -= 1
gain = montant_final * taux_de_rendement_annuel /100
montant_final += gain
print(f"Gain: {gain}€, Montant final: {montant_final}€, Taux de rendement annuel: {taux_de_rendement_annuel}%.")






