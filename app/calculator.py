import pandas as pd

STATIC_EMISSIONS_FACTORS = {
    "car": 0.2,  # kg CO2 per km
    "train": 0.05,
    "plane": 0.5
}

def calculate_emissions(mode, distance_km):
    factor = STATIC_EMISSIONS_FACTORS.get(mode, 0)
    return round(factor * distance_km, 2)

def load_data():
    return pd.read_csv("app/basecarbone-v17-fr.csv")