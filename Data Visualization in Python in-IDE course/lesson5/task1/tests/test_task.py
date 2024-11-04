import pandas as pd

def test_ordering():
    df = pd.read_csv('../../../dataset.csv')
    platforms = ["PS4", "XOne", "PC", "WiiU"]
    filtered_df = df[df['platform'].isin(platforms)]
    genre_counts = filtered_df.groupby(['platform', 'genre']).size().unstack(fill_value=0)
    ordered_genre_counts = genre_counts.reindex(platforms)
    assert list(ordered_genre_counts.index) == platforms, "Platforms should be in the specified order."
    print("Platform order is correct!")

test_ordering()
