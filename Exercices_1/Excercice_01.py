# Ecrire un programme pour inverser le contenu d’une chaine de caractères.

reversed_str = ""
a = input("Entrez une chaine de caractères: ")
for char in a:
    reversed_str = char + reversed_str
print(reversed_str)
