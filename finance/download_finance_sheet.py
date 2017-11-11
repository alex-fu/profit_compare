# coding=utf-8

"""
1. 资产负债表
http://quotes.money.163.com/service/zcfzb_300438.html （报告期 季度累加）
http://quotes.money.163.com/service/zcfzb_300438.html?type=year
2. 利润表
http://quotes.money.163.com/service/lrb_300438.html
http://quotes.money.163.com/service/lrb_300438.html?type=year
3. 现金流量表
http://quotes.money.163.com/service/xjllb_300438.html
http://quotes.money.163.com/service/xjllb_300438.html?type=year

4. 主要财务指标
http://quotes.money.163.com/service/zycwzb_300438.html （季度累积）
http://quotes.money.163.com/service/zycwzb_300438.html?type=year
http://quotes.money.163.com/service/zycwzb_300438.html?type=season (单季度)

5. 财务报表摘要
http://quotes.money.163.com/service/cwbbzy_300438.html?type=year
http://quotes.money.163.com/service/cwbbzy_300438.html
"""


# download finance sheets
from utils.file_utils import create_path
from utils.net_utils import download_file


def download_all_financial_data(stock_code):
    base_path = "/Users/fuyifeng/finance/" + stock_code
    create_path(base_path)

    download_file(_get_url("zcfzb", "report", stock_code), _get_local_filename(base_path, "zcfzb", "report", stock_code, "csv"))
    download_file(_get_url("zcfzb", "year", stock_code), _get_local_filename(base_path, "zcfzb", "year", stock_code, "csv"))
    download_file(_get_url("lrb", "report", stock_code), _get_local_filename(base_path, "lrb", "report", stock_code, "csv"))
    download_file(_get_url("lrb", "year", stock_code), _get_local_filename(base_path, "lrb", "year", stock_code, "csv"))
    download_file(_get_url("xjllb", "report", stock_code), _get_local_filename(base_path, "xjllb", "report", stock_code, "csv"))
    download_file(_get_url("xjllb", "year", stock_code), _get_local_filename(base_path, "xjllb", "year", stock_code, "csv"))
    download_file(_get_url("zycwzb", "report", stock_code), _get_local_filename(base_path, "zycwzb", "report", stock_code, "csv"))
    download_file(_get_url("zycwzb", "year", stock_code), _get_local_filename(base_path, "zycwzb", "year", stock_code, "csv"))
    download_file(_get_url("zycwzb", "season", stock_code), _get_local_filename(base_path, "zycwzb", "season", stock_code, "csv"))
    download_file(_get_url("cwbbzy", "report", stock_code), _get_local_filename(base_path, "cwbbzy", "report", stock_code, "csv"))
    download_file(_get_url("cwbbzy", "year", stock_code), _get_local_filename(base_path, "cwbbzy", "year", stock_code, "csv"))


# private functions
def _get_local_filename(base_path, table_type, type, stock_code, ext):
    return "{}/{}_{}_{}.{}".format(base_path, table_type, type, stock_code, ext)


def _get_url(table_type, type, stock_code):

    if table_type == "zcfzb":  # 1. 资产负债表
        return _get_url_zcfzb(stock_code, type)
    elif table_type == "lrb":  # 2. 利润表
        return _get_url_lrb(stock_code, type)
    elif table_type == "xjllb":  # 3. 现金流量表
        return _get_url_xjllb(stock_code, type)
    elif table_type == "zycwzb":  # 4. 主要财务指标
        return _get_url_zycwzb(stock_code, type)
    elif table_type == "cwbbzy":  # 5. 财务报表摘要
        return _get_url_cwbbzy(stock_code, type)
    else:
        return None


def _get_url_zcfzb(stock_code, type=None):
    url = "http://quotes.money.163.com/service/zcfzb_" + stock_code + ".html"
    if type is not None:
        url += "?type=" + type

    return url


def _get_url_lrb(stock_code, type=None):
    url = "http://quotes.money.163.com/service/lrb_" + stock_code + ".html"
    if type is not None:
        url += "?type=" + type

    return url


def _get_url_xjllb(stock_code, type=None):
    url = "http://quotes.money.163.com/service/xjllb_" + stock_code + ".html"
    if type is not None:
        url += "?type=" + type

    return url


def _get_url_zycwzb(stock_code, type=None):
    url = "http://quotes.money.163.com/service/zycwzb_" + stock_code + ".html"
    if type is not None:
        url += "?type=" + type

    return url


def _get_url_cwbbzy(stock_code, type=None):
    url = "http://quotes.money.163.com/service/cwbbzy_" + stock_code + ".html"
    if type is not None:
        url += "?type=" + type

    return url


if __name__ == "__main__":
    stock_list = ['300438', '002074', '300116']
    map(lambda stock: download_all_financial_data(stock), stock_list)


