import munch
import requests
import json
import time
import step1
import step2
import annualized_growth_rate as annual
import cagr
import cup

response = requests.get('https://financialmodelingprep.com/api/v3/company/stock/list')
symbolsList = response.json().get("symbolsList")
# print(symbolsList)

for symbols in symbolsList:
	# print(symbols.get('symbol'))
	if(symbols.get('exchange') == 'New York Stock Exchange' or symbols.get('exchange') == 'Nasdaq Global Select'):
	# if(symbols.get('exchange') == 'Toronto'):
		# sym = symbols.get('symbol').split(".")
		sym = symbols.get('symbol')
		print(sym)
		time.sleep(2)
		quaterly_eps = step1.calc_eps(sym)
		
		if quaterly_eps is not None:
			
			annual.calc_annual_eps(sym)
			cagr.calc_cagr(sym)
			cup.cup(sym)
