def entier():
    entier = [1, 2, 3, 4, 5]
    entier[0],entier[4] = entier[4], entier [0]
    # temp = entier[0]
    # entier[0] = entier[4]
    # entier[4] = temp
    print(entier)
    return entier
entier()