import pandas as pd

def test_filter():
    df = pd.read_csv('../../../dataset.csv')
    platforms = ["PS4", "XOne", "PC", "WiiU"]
    filtered_df = df[df['platform'].isin(platforms)]
    assert all(filtered_df['platform'].isin(platforms)), "Data should only include specified platforms."
    print("Data filtered successfully!")

test_filter()

