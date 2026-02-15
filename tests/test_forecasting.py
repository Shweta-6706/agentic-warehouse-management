from src.forecasting import moving_average_forecast, calculate_volatility

def test_moving_average():
    data = [10, 20, 30, 40, 50]
    result = moving_average_forecast(data, window=5)
    assert result == 30

def test_volatility():
    data = [10, 10, 10, 10, 10]
    result = calculate_volatility(data)
    assert result == 0

