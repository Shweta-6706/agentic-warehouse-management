def classify_risk(current_stock, reorder_point):
    """
    Classify product risk level based on stock vs ROP.
    """
    if current_stock < reorder_point:
        return "CRITICAL"
    elif current_stock < 1.2 * reorder_point:
        return "WARNING"
    else:
        return "SAFE"


def calculate_priority_score(depletion_days, volatility, growth_rate):
    score = 0

    # Depletion impact (max 50 points)
    if depletion_days < 3:
        score += 50
    elif depletion_days < 7:
        score += 30
    elif depletion_days < 14:
        score += 15

    # Volatility impact (max 25 points)
    score += min(volatility / 2, 25)

    # Growth impact (max 25 points)
    if growth_rate > 0:
        score += min(growth_rate * 2, 25)

    return float(round(score, 2))



def generate_recommendation(product_id,
                            current_stock,
                            avg_demand,
                            reorder_point,
                            eoq,
                            depletion_days,
                            risk_level,
                            growth_rate):
    """
    Generate natural language explanation.
    """

    if risk_level == "CRITICAL":
        action = "Immediate reorder required."
        suggested_qty = round(eoq)
    elif risk_level == "WARNING":
        action = "Monitor closely and prepare to reorder."
        suggested_qty = round(eoq * 0.75)
    else:
        action = "Stock levels are stable."
        suggested_qty = 0

    explanation = (
        f"Product {product_id} shows a growth rate of {growth_rate:.2f}%.\n"
        f"Current stock will last approximately {depletion_days:.2f} days.\n"
        f"Risk Level: {risk_level}.\n"
        f"Recommended Order Quantity: {suggested_qty} units.\n"
        f"Action: {action}"
    )

    return explanation

