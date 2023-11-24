def my_long_word(length_threshold, input_string):
    resultat = ""
    mot = ""
    space = True  
    for char in input_string:
        if char == ' ':
            if not space:
                if len(mot) > length_threshold:
                    resultat += mot + ' '
                mot = ""
            space = True
        else:
            mot += char
            space = False
    if len(mot) > length_threshold:
        resultat += mot
    return resultat.strip()  
threshold = 3
input_text = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
output_text = my_long_word(threshold, input_text)

print(output_text)
