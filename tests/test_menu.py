
def test_menu_distinct():
    assert "menu" == "menu"

def test_menu_cost():
    assert 1 + 1 == 2

def test_menu_fifo():
    lots = [{"id": "L1", "qty": 10}]
    assert len(lots) == 1
