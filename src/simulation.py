def apply_demand_change(demand_history, percent_change):
    """
    Increase or decrease demand by percentage.
    percent_change = +20 means +20% demand
    """
    factor = 1 + (percent_change / 100)
    return [d * factor for d in demand_history]


def apply_lead_time_delay(original_lead_time, delay_days):
    """
    Add delay to lead time.
    """
    return original_lead_time + delay_days


def apply_demand_spike(demand_history, spike_multiplier=1.5):
    """
    Simulate sudden spike in last few days.
    """
    new_history = demand_history.copy()
    for i in range(-3, 0):  # last 3 days spike
        new_history[i] *= spike_multiplier
    return new_history

