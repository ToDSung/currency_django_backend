# coding: utf-8

import requests
from pyquery import PyQuery as pq
import pandas as pd
import configparser 
import time
from sqlalchemy import create_engine


def run_crawler(currency_eng):

    #currency_eng = {'JPY': '日幣', 'CNY': '人民幣', 'HKD': '港幣', 'USD': '美金', 'EUR': '歐元', 'GBP': '英鎊', 'AUD': '澳幣', 'SGD': '新加坡幣', 'KRW': '韓元'}
    #currency_eng = 'JPY'

    
    url = 'https://rate.bot.com.tw/xrt/quote/l6m/{}'.format(currency_eng)
    print(url)
    history_page_source = requests.get(url)
    doc = pq(history_page_source.text)
    date_list = []
    rate_cash_buy_list = []
    rate_cash_sell_list = []
    rate_sight_buy_list = []
    rate_sight_sell_list = []
    for currency in doc('tr').items():
        date_list.append(currency('.text-center').eq(0).text())
        rate_cash_buy_list.append(currency('.rate-content-cash').eq(0).text())
        rate_cash_sell_list.append(currency('.rate-content-cash').eq(1).text())
        rate_sight_buy_list.append(currency('.rate-content-sight').eq(0).text())
        rate_sight_sell_list.append(currency('.rate-content-sight').eq(1).text())

    currency_dict = {'date': date_list, 'rate_cash_buy': rate_cash_buy_list, 'rate_cash_sell': rate_cash_sell_list, 'rate_sight_buy': rate_sight_buy_list, 'rate_sight_sell': rate_sight_sell_list}
    currency_df = pd.DataFrame.from_dict(currency_dict)
    currency_df = currency_df.drop(currency_df.index[0])
    currency_df = currency_df.drop(currency_df.index[0])
    # count data 

    # currency_df['DateValue'] = currency_df['DateValue'].astype('float64')
    # currency_data = {}
    # currency_data['{} 本日現金賣出匯率'.format(currencies_eng[currency_eng_value])] = currency_df['DateValue'].iloc[0]
    # currency_data['{} 半年內最高匯率'.format(currencies_eng[currency_eng_value])] = currency_df['DateValue'].max()
    # currency_data['{} 半年內最低匯率'.format(currencies_eng[currency_eng_value])] = currency_df['DateValue'].min()
    # currency_data['{} 半年內匯率 10% 價格'.format(currencies_eng[currency_eng_value])] = currency_df['DateValue'].quantile(.1)
    # currency_data['{} 半年內匯率中位數'.format(currencies_eng[currency_eng_value])] = currency_df['DateValue'].quantile(.5)
    # currency_data['{} 半年內匯率 90% 價格'.format(currencies_eng[currency_eng_value])] = currency_df['DateValue'].quantile(.9)
    # currency_data['{} 半年內詳細資料'.format(currencies_eng[currency_eng_value])] = url
    
    
    #time.sleep(5)
    return currency_df


if __name__ == '__main__':
    engine = create_engine('sqlite:///./currency_web_backend//db.sqlite3', echo=False)
    currencies_eng = ['JPY', 'CNY', 'HKD', 'USD', 'EUR', 'GBP', 'AUD', 'SGD', 'KRW']
    for currency_eng in currencies_eng:
        df = run_crawler(currency_eng)
        time.sleep(5)
        print('currency_data_{}'.format(currency_eng.lower()))
        df.to_sql('currency_data_{}'.format(currency_eng.lower()), con = engine, if_exists='replace', index=False)
        