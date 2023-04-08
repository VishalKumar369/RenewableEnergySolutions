import pandas as pd

def read_energy_data():
    """
    Reads the energy-related dataset from the given file path.
    """
    data = pd.read_csv("hourly_electricity_demand.csv")
    return data