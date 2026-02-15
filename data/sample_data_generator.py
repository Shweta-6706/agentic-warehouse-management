import pandas as pd
import numpy as np

def generate_sample_data(num_products=50):
    np.random.seed(42)

    data = []

    for i in range(num_products):
        product_id = f"P{i+1:03d}"
        current_stock = np.random.randint(50, 500)
        lead_time = np.random.randint(2, 10)
        ordering_cost = np.random.uniform(50, 200)
        holding_cost = np.random.uniform(1, 5)
        warehouse_capacity = 1000
        historical_demand = np.random.randint(10, 60, 30).tolist()

        data.append({
            "product_id": product_id,
            "current_stock": current_stock,
            "lead_time": lead_time,
            "ordering_cost": ordering_cost,
            "holding_cost": holding_cost,
            "warehouse_capacity": warehouse_capacity,
            "historical_demand": historical_demand
        })

    df = pd.DataFrame(data)
    df.to_csv("data/warehouse_data.csv", index=False)
    print("Sample dataset created successfully.")

if __name__ == "__main__":
    generate_sample_data()

