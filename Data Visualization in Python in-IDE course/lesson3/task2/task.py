import pandas as pd

# Load dataset
df = pd.read_csv('../../dataset.csv')

# Filter by specific platforms
platforms = ["PS4", "XOne", "PC", "WiiU"]
filtered_df = df[df['platform'].isin(platforms)]
print(filtered_df)
