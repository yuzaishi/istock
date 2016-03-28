#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#    > Author: Light.Zhang
#    > Mail: zhilight@gmail.com
#    > Created Time: 16/01/12 14:00:01

from yahoo_finance import Share
import tushare


def get_data():
    pass


def get_data_demo():
    yahoo = Share('YHOO')
    print(yahoo.get_open())
    print(yahoo.get_price())
    print(yahoo.get_trade_datetime())


def refresh_data_demo():
    yahoo = Share('YHOO')
    print(yahoo.get_open())
    print(yahoo.get_price())
    print(yahoo.get_trade_datetime())
    yahoo.refresh()
    print('Refresh data.')
    yahoo = Share('YHOO')
    print(yahoo.get_open())
    print(yahoo.get_price())
    print(yahoo.get_trade_datetime())


def main():
    get_data_demo()
    refresh_data_demo()


if __name__ == '__main__':
    main()