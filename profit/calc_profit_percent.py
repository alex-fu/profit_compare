import pandas as pd


def join_by_code(year):
    df1 = pd.read_csv("./reports" + year + ".csv", dtype={'code': 'object'})
    # print(df1)
    df2 = pd.read_csv("./" + year, dtype={'code': 'object'})
    # print(df2)
    merged = pd.merge(df1, df2, how='left', on='code')
    # merged = merged.ix[merged.profits_yoy > 0]
    merged['PE'] = merged['end'] / merged['eps']
    merged['PB'] = merged['end'] / merged['bvps']
    merged['dividend'] = merged['profits_yoy'] / merged['percent']
    merged.sort_values('dividend', inplace=True, ascending=False)
    merged.to_csv("./merged" + year + ".csv", encoding='utf-8')


join_by_code('2014')
join_by_code('2015')
join_by_code('2016')
join_by_code('2017')
