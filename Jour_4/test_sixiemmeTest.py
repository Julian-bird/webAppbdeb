import pytest

@pytest.mark.regression
def test_one():
    print("caseOne")
@pytest.mark.regression
def test_two():
    print("caseTwo")
@pytest.mark.charger
def test_three():
    print("caseThree")
@pytest.mark.skip
def test_four():
    print("caseFour")
@pytest.mark.charger
def test_five():
    print("caseFive")