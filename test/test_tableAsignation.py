import pytest
from src.tableAsignation import tableAsignation

@pytest.mark.getTable
def test_getTable():
    assert tableAsignation().getTable() == ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

@pytest.mark.check_lenght_tableAsignation
def test_check_lenght_tableAsignation():
    assert len(tableAsignation().getTable()) == 23
