import pytest
from src.Dni import Dni

##Tests for the functions:
#Tests for the basics operations:
@pytest.mark.getDni
def test_getDni():
    assert Dni('60422243R').getDni() == '60422243R'

@pytest.mark.getNumberDni
def test_getNumbersDni():
    assert Dni('86709130G').getNumberDni() == '86709130'

@pytest.mark.getLetterDni
def test_getLetterDni():
    assert Dni('20090860S').getLetterDni() == 'S'

#Tests most importants for the last steps:
@pytest.mark.calculateLetterDni
def test_calculateLetterDni():
    assert Dni('17804654D').calculateLetterDni() == 'D'

@pytest.mark.checkDni
def test_checkDni():
    assert Dni('22475074A').checkDni() == True
    assert Dni('22475074B').checkDni() == False


#Tests for basics verifications:
@pytest.mark.check_lenght_Dni
def test_check_lenght_Dni():
    assert len(Dni('26822006G').getDni()) == Dni().LENGHT_DNI

@pytest.mark.check_lenght_numbers_Dni
def test_check_lenght_numbers_Dni():
    assert len(Dni('26822006G').getNumberDni()) == Dni().LENGHT_NUMBER_DNI
