import pandas as pd
import matplotlib.pyplot as plt

# Load and filter dataset
df = pd.read_csv('../../dataset.csv')
platforms = ["PS4", "XOne", "PC", "WiiU"]
filtered_df = df[df['platform'].isin(platforms)]

# Group data by genre and platform
genre_counts = filtered_df.groupby(['platform', 'genre']).size().unstack(fill_value=0)

# Plotting
genre_counts.plot(kind='bar', figsize=(10, 7))
plt.xlabel("Genre")
plt.ylabel("Number of Games")
plt.title("Number of Games per Genre across Platforms")
plt.legend(title="Platform")
plt.show()
