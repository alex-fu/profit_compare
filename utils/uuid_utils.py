# coding=utf-8

from xid import Xid


def get_uuid():
    return Xid().string()


