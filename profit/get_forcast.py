import tushare as ts

forcast = ts.forecast_data(2017, 3)
forcast.set_index('code', inplace=True)

forcast.to_csv('./forcast201703.csv', encoding='utf-8')
