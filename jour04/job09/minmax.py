def liste():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    max = L[0]
    min = L[0]
    for n in L:
        if n > max:
            max = n
    print("La plus grande valeur est:",max)
    for x in L:
        if x < min:
            min = x    
    print("La plus petite valeur est:",min)
liste()

