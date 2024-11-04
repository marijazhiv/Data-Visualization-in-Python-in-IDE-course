import pandas as pd
import matplotlib.pyplot as plt

# Load and filter dataset
df = pd.read_csv('../../dataset.csv')
platforms = ["PS4", "XOne", "PC", "WiiU"]
filtered_df = df[df['platform'].isin(platforms)]

# Group and reorder data by genre and platform
genre_counts = filtered_df.groupby(['platform', 'genre']).size().unstack(fill_value=0)
genre_counts = genre_counts.reindex(platforms).sort_index(axis=1)

# Plotting with custom order
genre_counts.plot(kind='bar', figsize=(10, 7), color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
plt.xlabel("Genre")
plt.ylabel("Number of Games")
plt.title("Number of Games per Genre across Platforms")
plt.legend(title="Platform")
plt.show()
