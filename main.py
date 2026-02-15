import argparse
import pandas as pd
from src.data_loader import load_data
from src.forecasting import (
    moving_average_forecast,
    calculate_volatility,
    demand_growth_rate
)
from src.optimization import (
    calculate_safety_stock,
    calculate_reorder_point,
    calculate_eoq,
    estimate_depletion_days
)
from src.agent import (
    classify_risk,
    calculate_priority_score
)
from src.simulation import (
    apply_demand_change,
    apply_lead_time_delay,
    apply_demand_spike
)


def run_agent(data_path, demand_increase, lead_delay, spike):
    df = load_data(data_path)
    results = []

    for _, product in df.iterrows():

        simulated_demand = product["historical_demand"]

        # Apply simulations
        simulated_demand = apply_demand_change(simulated_demand, demand_increase)

        if spike:
            simulated_demand = apply_demand_spike(simulated_demand)

        simulated_lead_time = apply_lead_time_delay(product["lead_time"], lead_delay)

        # Forecast
        avg_demand = moving_average_forecast(simulated_demand)
        volatility = calculate_volatility(simulated_demand)
        growth_rate = demand_growth_rate(simulated_demand)

        # Optimization
        safety_stock = calculate_safety_stock(volatility, simulated_lead_time)
        rop = calculate_reorder_point(avg_demand, simulated_lead_time, safety_stock)

        annual_demand = avg_demand * 365
        eoq = calculate_eoq(annual_demand, product["ordering_cost"], product["holding_cost"])

        depletion_days = estimate_depletion_days(product["current_stock"], avg_demand)

        # Agent
        risk_level = classify_risk(product["current_stock"], rop)

        priority_score = calculate_priority_score(
            depletion_days,
            volatility,
            growth_rate
        )

        results.append({
            "product_id": product["product_id"],
            "priority_score": priority_score,
            "risk_level": risk_level,
            "depletion_days": float(round(depletion_days, 2)),
            "recommended_order_qty": int(eoq)
        })

    ranked = sorted(results, key=lambda x: x["priority_score"], reverse=True)
    report_df = pd.DataFrame(ranked)
    report_df.to_csv("warehouse_priority_report.csv", index=False)
    print("\nReport saved as warehouse_priority_report.csv")


    print("\n==============================")
    print("WAREHOUSE PRIORITY REPORT")
    print("==============================\n")

    for item in ranked[:5]:
        print(item)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Warehouse Management Agent")

    parser.add_argument("--data", type=str, default="data/warehouse_data.csv")
    parser.add_argument("--demand_increase", type=float, default=0)
    parser.add_argument("--lead_delay", type=int, default=0)
    parser.add_argument("--spike", action="store_true")

    args = parser.parse_args()

    run_agent(
        args.data,
        args.demand_increase,
        args.lead_delay,
        args.spike
    )
