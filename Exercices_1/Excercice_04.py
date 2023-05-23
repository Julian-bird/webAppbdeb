#Ecrire un programme pour vérifier si deux chaînes données sont anagrammes ou pas?

str1 = input("Entrez premier chaine de caractères: ")
str2 = input("Entrez deuxième chaine de caractères: ")
str1_sort = sorted(str1)
str2_sort = sorted(str2)
if str1_sort == str2_sort:
    print("Les deux chaînes sont anagrammes.")
else:
    print("Les deux chaînes ne sont pas anagrammes.")
