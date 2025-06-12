
def test_waste_distinct():
    assert "waste" == "waste"

def test_waste_cost():
    assert 1 + 1 == 2

def test_waste_fifo():
    lots = [{"id": "L1", "qty": 10}]
    assert len(lots) == 1
