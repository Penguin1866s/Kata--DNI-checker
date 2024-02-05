from src.tableAsignation import tableAsignation

@pytest.mark.check_lenght_tableAsignation
def test_check_lenght_tableAsignation():
    assert len(tableAsignation().getTable) == 23
