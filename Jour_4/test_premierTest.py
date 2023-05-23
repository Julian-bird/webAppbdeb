"""
1: Installer "pytest" ==> pip install pytest
2：Creer un fichier python ==> Doit contenir le mot "test" au debut
3: Importer le package "pytest"
4: pytest Jour_4/test_premierTest.py
5: pytest Jour_4/test_premierTest.py -s -v
"""
import pytest

def test_login():
    print("ce connecter sur google")
def test_creerCompte():
    print("creation compte")