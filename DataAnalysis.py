import pandas as pd
import matplotlib.pyplot as plt
from Api1 import read_energy_data


# Get energy data from API
energy_data = read_energy_data()

# Convert JSON energy data to Pandas DataFrame
df_energy = pd.DataFrame(energy_data)

# Plot energy production over time
plt.plot(df_energy['Hour'], df_energy['Electricity Demand'])
plt.title('Energy Production Over Time')
plt.xlabel('Hour')
plt.ylabel('Production (kWh)')
plt.show()

# Calculate average daily energy production
avg_daily_production = df_energy['production'].mean()
print(f'Average daily production: {avg_daily_production} kWh')