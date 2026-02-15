import numpy as np

def moving_average_forecast(demand_history, window=7):
    """
    Calculate moving average forecast.
    demand_history: list of past demand values
    window: number of days for moving average
    """
    if len(demand_history) < window:
        return np.mean(demand_history)

    return np.mean(demand_history[-window:])


def calculate_volatility(demand_history):
    """
    Measure demand variability (standard deviation).
    """
    return np.std(demand_history)


def demand_growth_rate(demand_history):
    """
    Calculate percentage growth between first half and second half.
    """
    midpoint = len(demand_history) // 2
    first_half = np.mean(demand_history[:midpoint])
    second_half = np.mean(demand_history[midpoint:])

    if first_half == 0:
        return 0

    growth = ((second_half - first_half) / first_half) * 100
    return growth


