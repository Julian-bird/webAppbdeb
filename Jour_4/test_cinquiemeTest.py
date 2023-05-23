import pytest

@pytest.fixture(scope="module")
def setup():
    print("ouvrire la base de doner")
    yield
    print("fermer la base de doner")
@pytest.fixture(scope="function")   
def before():
    print("ouvrire le navigateur")
    yield
    print("fermer le navigateur")
#======================================================================================
#======================================================================================
@pytest.mark.usefixtures("setup","before")
def test_login():
    print("ce connecter sur google")
@pytest.mark.usefixtures("setup","before")
def test_creerCompte():
    print("creation compte")
@pytest.mark.usefixtures("setup","before")
def test_motDePass():
    print("reenitialiserPPass")