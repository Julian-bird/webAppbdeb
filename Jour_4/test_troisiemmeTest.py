### include 4 def below；
# def setup_function(function):
#     print("ouvrire le navigateur")
#
# def teardown_function(function):
#     print("fermer le navigateur")
#
# def setup_module(module):
#     print("ouvrire la base de doner")
#
# def teardown_module(module):
#     print("fermer la base de doner")

import pytest

@pytest.fixture(scope="module")
def setup():
    print("ouvrire la base de doner")
    yield
    print("fermer la base de doner")
@pytest.fixture(scope="function")   
def setupfunc():
    print("ouvrire le navigateur")
    yield
    print("fermer le navigateur")
#======================================================================================
#======================================================================================
def test_login(setup,setupfunc):
    print("ce connecter sur google")

def test_creerCompte(setup,setupfunc):
    print("creation compte")

def test_motDePass():
    print("reenitialiserPPass")