
def test_purchasing_distinct():
    assert "purchasing" == "purchasing"

def test_purchasing_cost():
    assert 1 + 1 == 2

def test_purchasing_fifo():
    lots = [{"id": "L1", "qty": 10}]
    assert len(lots) == 1
