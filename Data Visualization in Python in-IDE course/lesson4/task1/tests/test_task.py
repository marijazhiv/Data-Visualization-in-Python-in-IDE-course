import pandas as pd

def test_plot_data():
    df = pd.read_csv('../../../dataset.csv')
    platforms = ["PS4", "XOne", "PC", "WiiU"]
    filtered_df = df[df['platform'].isin(platforms)]
    genre_counts = filtered_df.groupby(['platform', 'genre']).size().unstack(fill_value=0)
    assert not genre_counts.empty, "Grouped data should not be empty after grouping."
    print("Data grouped successfully!")

test_plot_data()
