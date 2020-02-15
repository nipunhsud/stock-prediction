import munch
import requests
import json

response = requests.get('https://financialmodelingprep.com/api/v3/financials/income-statement/TSLA?period=quarter')

data = response.json()

# print(data)

a = munch.Munch(data)


financialList = data.get('financials')

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
print(a.financials[0])

v2 = a.financials[0].get('EPS')
v1 =financialList[4].get('EPS')
print("From "+ financialList[0].get('date') + " to "+ financialList[4].get('date'))
print(((float(v2) - float(v1))/float(v1))* 100)

