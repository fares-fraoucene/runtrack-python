def liste(type, saison):
    fruits = {"hiver": "orange, mandarine et kiwi", "ete": "Poire, fraise, cassis"}
    legumes = {"hiver": "carotte, topinambour, endive", "ete": "artichaut, aubergine,navet" }
    if type == "fruits":
        print(fruits[saison])
    elif type == "legumes":
        print(legumes[saison])
        
liste("fruits", "ete")
liste("legumes", "hiver")
