def tri_bulle(liste):
    a = 0
    for _ in liste:
        a += 1
    b = 0
    while b < a:
        c = 0
        while c < a - b -1:
            if liste[c] > liste[c +1 ]:
                liste[c], liste[c + 1] = liste[c + 1], liste[c]
            c += 1
        b += 1 
        
L = [8, 4,9,15,261,55,1,350,7,3]
tri_bulle(L)
print(L)