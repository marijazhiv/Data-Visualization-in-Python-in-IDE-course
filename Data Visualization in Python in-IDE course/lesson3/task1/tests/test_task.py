import pandas as pd

def test_load():
    try:
        df = pd.read_csv('../../../dataset.csv')
        assert not df.empty, "The dataset should be loaded and not be empty."
        print("Dataset loaded successfully!")
    except Exception as e:
        print(f"Loading failed: {e}")

test_load()

