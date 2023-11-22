def pair_impair(num):
    if type(num) == int and num > 0:
        if num % 2 == 0:
            print("Pair")
        else:
            print("Impair")
    else:
        print("Erreur de saisie")
        
pair_impair(4321)
pair_impair(1234)
pair_impair(-4444)