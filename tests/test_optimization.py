from src.optimization import calculate_eoq

def test_eoq_basic():
    annual_demand = 1000
    ordering_cost = 50
    holding_cost = 2

    eoq = calculate_eoq(annual_demand, ordering_cost, holding_cost)

    assert eoq > 0

