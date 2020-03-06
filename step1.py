import munch
import requests
import json

def calc_eps(stock):
	# print('https://financialmodelingprep.com/api/v3/financials/income-statement/{}?period=quarter'.format(stock))
	response = requests.get('https://financialmodelingprep.com/api/v3/financials/income-statement/{}?period=quarter'.format(stock))

	data = response.json()

	# print(data)

	a = munch.Munch(data)
	financialList = []
	if 'financials' in data:
		financialList = data.get('financials')
		if len(financialList) > 4:
			v2 = a.financials[0].get('EPS')
			v1 =financialList[4].get('EPS')
			if '-' in v2:
				v2 = 0
			if v2 != '' and v1 != '' and v1 != '0.0' and v1 != '-0.0':
				# print("From "+ financialList[0].get('date') + " to "+ financialList[4].get('date'))
				quaterly_eps = ((float(v2) - float(v1))/float(v1))* 100
				if(quaterly_eps > 20):
					# print(quaterly_eps)
					print('Quaterly annualized growth rate % '+ str(quaterly_eps))
					return quaterly_eps
	# print(a.financials)
	# print(a.financials[0].get('date'))
	# for financial in a.financials:
	# 	b = munch.Munch(financial)
	# 	financialList[b.get('date')] = b.get('EPS')

	# print(financialList)


	# percentageIncrease = ((float(financialList.get('2019-09-30')) - float(financialList.get('2018-09-30'))) / float(financialList.get('2018-09-30')) * 100)
			
	# print("======")
	# print(percentageIncrease)
	# print("======")

	# print(len(financialList))s
	# print(a.financials[0])

	

