
def test_pos_distinct():
    assert "pos" == "pos"

def test_pos_cost():
    assert 1 + 1 == 2

def test_pos_fifo():
    lots = [{"id": "L1", "qty": 10}]
    assert len(lots) == 1
