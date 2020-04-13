import munch
import requests
import json
import time
from dateutil.relativedelta import relativedelta
import datetime

def calc_eps(stock):
	response = requests.get('https://financialmodelingprep.com/api/v3/financials/income-statement/{}?period=quarter'.format(stock))

	data = response.json()

	# print(data)
	
   
	a = munch.Munch(data)
	financialList = []
	if 'financials' in data:
		financialList = data.get('financials')
		if datetime.datetime.strptime(financialList[0].get('date'), '%Y-%m-%d') < datetime.datetime.today() + relativedelta(days=-365):
			return None
 
		if len(financialList) > 4:
			v2 = a.financials[0].get('EPS')
			v1 =financialList[4].get('EPS')
			if '-' in v2:
				v2 = 0
			if v2 != '' and v1 != '' and v1 != '0.0' and v1 != '-0.0':
				# print("From "+ financialList[0].get('date') + " to "+ financialList[4].get('date'))
				quaterly_eps = ((float(v2) - float(v1))/float(v1))* 100
				return quaterly_eps


	

