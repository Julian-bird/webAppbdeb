# Ecrire un programme pour inverser l'ordre des mots présents dans une Chaîne de caractère?

a = input("Entrez une chaine de caractères: ")
words = a.split()
reversed_words = ""
for char in words:
    reversed_words = char + " " + reversed_words
print(reversed_words)
