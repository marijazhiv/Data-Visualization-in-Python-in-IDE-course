def test_environment():
    try:
        import pandas
        import matplotlib.pyplot
        import plotly
        print("Environment setup is correct!")
    except ImportError:
        print("Some libraries are missing. Please check your installation.")

test_environment()
