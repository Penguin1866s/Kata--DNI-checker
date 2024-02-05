import pytest
from src.tableAsignation import tableAsignation
from list_dnis import list_dnis

##Tests for the functions:
#Tests for the basics operations:
@pytest.mark.getDni
def test_getDni():
    assert Dni('60422243R').getDni == '60422243R'

@pytest.mark.getNumberDni
def test_getNumbersDni():
    assert Dni('86709130G').getNumberDni == '86709130G'

@pytest.mark.getLetterDni
def test_getLetterDni():
    assert Dni('20090860S').getLetterDni == 'S'

#Tests most importants for the last steps:
@pytest.mark.calculateLetterDni
def test_calculateLetterDni():
    assert Dni('17804654D').calculateLetterDni == 'D'

@pytest.mark.checkDni
def checkDni():
    assert Dni('22475074A').checkDni == True


#Tests for basics verifications:
@pytest.mark.check_lenght
def test_check_lenght():
    assert len(Dni('26822006G').getDni) == 9
