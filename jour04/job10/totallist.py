def paire():    
    somme = 1
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    for n in L:
        if n >= 25 and n <= 90: 
            somme *= n
    print(somme)
paire()
