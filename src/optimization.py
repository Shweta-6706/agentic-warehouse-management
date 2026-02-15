import numpy as np

def calculate_safety_stock(volatility, lead_time, service_level_factor=1.65):
    """
    Safety Stock Formula:
    SS = Z × σ × sqrt(Lead Time)

    Z = service level factor (1.65 ≈ 95% service level)
    σ = demand standard deviation
    """
    return service_level_factor * volatility * np.sqrt(lead_time)


def calculate_reorder_point(avg_demand, lead_time, safety_stock):
    """
    ROP = (Average Demand × Lead Time) + Safety Stock
    """
    return (avg_demand * lead_time) + safety_stock


def calculate_eoq(annual_demand, ordering_cost, holding_cost):
    """
    EOQ = sqrt( (2DS) / H )
    """
    if holding_cost == 0:
        return 0
    return np.sqrt((2 * annual_demand * ordering_cost) / holding_cost)


def estimate_depletion_days(current_stock, avg_daily_demand):
    """
    Estimate how many days current stock will last.
    """
    if avg_daily_demand == 0:
        return float("inf")

    return current_stock / avg_daily_demand

