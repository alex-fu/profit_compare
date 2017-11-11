import tushare as ts
import pandas as pd

# stocks = ts.get_stock_basics()
#
# stocks.to_csv('./stocks.csv', encoding='utf-8')
# print(stocks)

# print(10 * "=")


def get_report_data(year):
    if year < 2017:
        df = ts.get_report_data(year, 4)
    else:
        df = ts.get_report_data(year, 2)
    df.drop_duplicates(subset='code', inplace=True)
    df.sort_values(["profits_yoy"], inplace=True, ascending=False)
    df.set_index('code', inplace=True)
    return df


def loop_retrieve_report_data(year):
    print("loop retrieve report data for " + str(year))
    filename = './reports' + str(year) + '.csv'
    dfall = None
    dfall_size = 0
    retry = 5
    while True:
        df = get_report_data(year)
        retry = retry - 1
        if dfall is None:
            dfall = df
        else:
            dfall = pd.concat([dfall, df])
            dfall = dfall[~dfall.index.duplicated()]
            dfall.sort_values(["profits_yoy"], inplace=True, ascending=False)

        size = len(dfall.index)
        print("=> size: " + str(size))

        if retry > 0 or size > dfall_size:
            dfall_size = size
            continue

        break

    dfall.to_csv(filename, encoding='utf-8')


if __name__ == '__main__':
    for year in [2014, 2015, 2016, 2017]:
        loop_retrieve_report_data(year)
