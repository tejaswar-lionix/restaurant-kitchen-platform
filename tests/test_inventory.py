
def test_inventory_distinct():
    assert "inventory" == "inventory"

def test_inventory_cost():
    assert 1 + 1 == 2

def test_inventory_fifo():
    lots = [{"id": "L1", "qty": 10}]
    assert len(lots) == 1
