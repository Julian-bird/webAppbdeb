# Ecrire un programme pour supprimer les caractères en double d’une chaîne de caractère?

a = input("Entrez une chaine de caractères: ")
unique_chars = ""
for char in a:
    if char not in unique_chars:
        unique_chars = unique_chars + char
print(unique_chars)
