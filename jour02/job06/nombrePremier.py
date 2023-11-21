for i in range(2, 1001):
    isprims = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            isprims = False
    if isprims == True or i == 2:
        print(i)
        

