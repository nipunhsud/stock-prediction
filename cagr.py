import munch
import requests
import json

# Gets the average annual eps growth over 5 years


def cagr(data, key):
    # print(data)
    # print(len(data))
    if(len(data) > 5):
        current_eps = munch.Munch(data[0]).get(key)
        five_year_eps = munch.Munch(data[5]).get(key)
        if '0.00' not in five_year_eps and five_year_eps != '0.0' and five_year_eps != '' and current_eps != '':
            if '-' in current_eps:
                current_eps = '0'
            cagr = (pow((float(current_eps.strip())/float(five_year_eps.strip())), 1/5) - 1) * 100
            return cagr


def calc_cagr(stock):
    # print(stock)
    annual_response = requests.get("https://financialmodelingprep.com/api/v3/financials/income-statement/{}".format(stock))
    annual_data = annual_response.json()
    annual_income_stmt = munch.Munch(annual_data)
    # print(annual_income_stmt)

    # Creates a ranker - this measures if EPS growth is more than 60%
    if 'financials' in annual_income_stmt:
        # print(annual_income_stmt.financials)
        return cagr(annual_income_stmt.financials, 'EPS')
