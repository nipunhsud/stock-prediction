import munch
import requests
import json
import runner


response = requests.get('https://financialmodelingprep.com/api/v3/company/stock/list')
symbolsList = response.json().get("symbolsList")
runner.analyze_stocks(symbolsList)
