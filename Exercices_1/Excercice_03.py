# Ecrire un programme pour vérifier si une chaîne de caractères est palindrome ou pas ?

reversed_str = ""
a = input("Entrez une chaine de caractères: ")
for char in a:
    reversed_str = char + reversed_str
print("La chaîne de caractères est palindrome : ",a==reversed_str)
