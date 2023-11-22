def moyenne(note1, note2, note3):
    return ((note1 + note2 + note3) / 3)

note1, note2, note3 = input("Espace entre chaque notes saisie:").split()
note1 = int(note1)
note2 = int(note2)
note3 = int(note3)
moyennes = moyenne(note1, note2, note3)

if 15 <= moyennes <= 20:
    print("Très bon élève")
elif 11 <= moyennes <= 14:
    print("Bon élève")
elif 8 <= moyennes <= 10:
    print("Élève moyen")
elif 0 <= moyennes <= 7:
    print("Élève devant faire des efforts")