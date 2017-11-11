import pandas as pd


def select_good_stock(df):
    return df.ix[df.net_profits > 0].ix[df.profits_yoy > 30]


def simple_df(year, df):
    df_simple = df[['code']].copy()
    df_simple['net_profits_' + year] = df['net_profits']
    df_simple['profits_yoy_' + year] = df['profits_yoy']
    df_simple['percent_' + year] = df['percent']
    return df_simple


if __name__ == "__main__":
    df14 = pd.read_csv("./merged2014.csv", dtype={'code': 'object'})
    df15 = pd.read_csv("./merged2015.csv", dtype={'code': 'object'})
    df16 = pd.read_csv("./merged2016.csv", dtype={'code': 'object'})
    df17 = pd.read_csv("./merged2017.csv", dtype={'code': 'object'})

    selected = select_good_stock(df17)

    # print(selected)
    # print(len(selected))

    joined = pd.merge(selected, simple_df("2016", df16), how='left', on='code')
    joined = pd.merge(joined, simple_df("2015", df15), how='left', on='code')
    joined = pd.merge(joined, simple_df("2014", df14), how='left', on='code')

    # print(joined)
    # print(len(joined))

    joined.to_csv("./joined2017.csv", encoding='utf-8')
