"""
1: ouvrire & fermer repeat
2: setup_function and teardown_function will run with each test(function)
3: setup_module and teardown_module only run one time
"""
import pytest

def setup_function(function):
    print("ouvrire le navigateur")

def teardown_function(function):
    print("fermer le navigateur")

def setup_module(module):
    print("ouvrire la base de doner")

def teardown_module(module):
    print("fermer la base de doner")

def test_login():
    # print("ouvrire le navigateur")
    print("ce connecter sur google")
    # print("fermer le navigateur")

def test_creerCompte():
    print("creation compte")

def test_motDePass():
    print("reenitialiserPPass")
