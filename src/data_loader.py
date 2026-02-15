import pandas as pd
import ast

def load_data(file_path):
    df = pd.read_csv("data/warehouse_data.csv")

    # Convert historical_demand string back to list
    df["historical_demand"] = df["historical_demand"].apply(ast.literal_eval)

    return df


