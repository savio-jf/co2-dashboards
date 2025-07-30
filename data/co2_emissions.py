import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('data/co2_emissions.csv')

# Clean data
df = df[df['Country'] != 'World']  # Optional

# Total emissions by year
yearly = df.groupby('Year')['Total'].sum().reset_index()

# Plot
fig = px.line(yearly, x='Year', y='Total', title='Global CO₂ Emissions Over Time')
fig.show()
