import munch
import requests
import json

response = requests.get('https://financialmodelingprep.com/api/v3/financials/income-statement/TSLA?period=quarter')

data = response.json()

print(type(data))

a = munch.Munch(data)


financialList = {}

print(a.financials)

for financial in a.financials:
	b = munch.Munch(financial)
	financialList[b.get('date')] = b.get('EPS')

print(financialList)

print(float(financialList['2019-09-30']))
percentageIncrease = ((float(financialList.get('2019-09-30')) - float(financialList.get('2018-09-30'))) / float(financialList.get('2018-09-30')) * 100)
		
print("======")
print(percentageIncrease)
print("======")

