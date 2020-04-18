import munch
import requests
import json
from dateutil.relativedelta import relativedelta
import datetime

def analyze(stock):
    from_date = datetime.date.today() + relativedelta(months=-15)
    to_date = datetime.date.today() + relativedelta(days=+1)
    # print(from_date)
    # print(to_date)
    stock_price_history = requests.get("https://financialmodelingprep.com/api/v3/historical-price-full/{}?from = {} & to = {}".format(stock, from_date, to_date)).json()
    # print(munch.Munch(stock_price_history).get('historical')[0])
    
    if munch.Munch(stock_price_history).get('historical') == None:
        return None
    current_price_index = len(munch.Munch(stock_price_history).get('historical')) - 1
    current_price = munch.Munch(stock_price_history).get('historical')[current_price_index].get('close')

    start_data = 0
    date_15_month_high_reached = 0
    for data in munch.Munch(stock_price_history).get('historical'):
        high_during_past_months = data.get('high')
        if high_during_past_months is None:
            high_during_past_months = 0
        if high_during_past_months > start_data:
            # print(data.get('high'))
            start_data = high_during_past_months
            date_15_month_high_reached = data.get('date')

    # print(current_price/high_during_past_months)
    price_ratio = 0
    if start_data > 1:
        price_ratio = current_price/start_data
    # print(date_15_month_high_reached)
    if price_ratio > .90 and price_ratio < 1.1:
        # print(datetime.datetime.strptime(
        #     date_15_month_high_reached, '%Y-%m-%d'))
        # print(datetime.datetime.today() + relativedelta(days=-45))
        # Returns yes, if the date it reached a 15month high was between 45 days and 15months from NOW
        if datetime.datetime.strptime(date_15_month_high_reached, '%Y-%m-%d') < datetime.datetime.today() + relativedelta(days=-40):
            return 'yes'
    # print(end_data/start_data)
    # print(stock_price_history)
