import time
import tushare as ts

from finance.download_finance_sheet import download_all_financial_data


def download_finance_all_stocks():
    stock_list = stock_code_all()

    # count = 0
    for stock in stock_list:
        download_all_financial_data(stock)
        time.sleep(1)
        # count += 1
        # if count >= 10:
        #     time.sleep(10)
        #     count = 0


def stock_code_all():
    df = ts.get_stock_basics()
    return df.sort_index().index


if __name__ == "__main__":
    download_finance_all_stocks()

