import pandas as pd
import plotly.express as px

# Step 1: Organize the Data
data = {
    "Country": ["España", "España", "España", "Portugal", "Portugal", "Portugal", "Francia", "Francia", "Francia", "Italia", "Italia", "Italia", "Centro Europa", "Centro Europa", "Centro Europa", "Polonia", "Polonia", "Polonia", "Mexico", "Mexico", "Mexico"],
    "Beverage": ["Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos", "Refrescos", "Isotonicas", "Zumos"],
    "2023": [12, 18, 22, 11, 17, 23, 13, 19, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "2024": [16, 24, 3, 16, 23, 31, 18, 26, 34, 16, 24, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "2025": [2, 28, 35, 2, 28, 36, 25, 3, 38, 24, 36, 45, 0, 0, 0, 0, 0, 0, 24, 36, 45],
    "2026": [2, 28, 35, 2, 28, 36, 25, 3, 38, 3, 4, 56, 0, 0, 0, 24, 28, 35, 3, 4, 5],
    "2027": [2, 28, 3, 2, 28, 3, 23, 28, 32, 24, 3, 34, 28, 34, 35, 26, 32, 38, 3, 29, 5],
    "2028": [25, 28, 29, 24, 28, 29, 27, 28, 3, 28, 31, 34, 28, 32, 32, 27, 32, 35, 32, 33, 38],
}


# Create DataFrame
df = pd.DataFrame(data)

# Step 2: Melt the DataFrame
df_melted = df.melt(id_vars=["Country", "Beverage"], var_name="Year", value_name="Price")

# Step 3: Create the Line Charts for each Beverage Type
for beverage_type in df['Beverage'].unique():
    df_filtered = df_melted[df_melted['Beverage'] == beverage_type]
    fig = px.line(df_filtered, x="Year", y="Price", color="Country", markers=True,
                  title=f"Price Levels of {beverage_type} by Country Over Time",
                  labels={"Year": "Year", "Price": "Price Level", "Country": "Country"})
    
    
    
    fig.show()