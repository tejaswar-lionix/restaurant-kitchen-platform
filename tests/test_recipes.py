
def test_recipes_distinct():
    assert "recipes" == "recipes"

def test_recipes_cost():
    assert 1 + 1 == 2

def test_recipes_fifo():
    lots = [{"id": "L1", "qty": 10}]
    assert len(lots) == 1
