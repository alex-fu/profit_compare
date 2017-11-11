import pandas as pd


def parse_forcast():
    df = pd.read_csv("./forcast201703.csv", dtype={'code': 'object'})
    print(df)

parse_forcast()
