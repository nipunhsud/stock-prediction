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

print(len(financialList))

for i in range(len(financialList)-4):

	v2 = financialList[i].EPS
	v1 =financialList[i+4].EPS
	v2_ebitda = financialList[i].EBITDA
	v1_ebitda = financialList[i+4].EBITDA
	print("From "+ financialList[i].date + " to "+ financialList[i+4].date)
	print(((float(v2) - float(v1))/float(v1))* 100)

annual_response = requests.get("https://financialmodelingprep.com/api/v3/financials/income-statement/TSLA")

annual_data = annual_response.json()

annual_income_stmt = munch.Munch(annual_data)

annual_financial_list = []
for financial in annual_income_stmt.financials:
	b = munch.Munch(financial)
	annual_financial_list.append(b)

for i in range (len(annual_financial_list)-1):
	v2 = annual_financial_list[i].EBITDA
	v1 = annual_financial_list[i+1].EBITDA
	v2_eps = annual_financial_list[i].EPS
	v1_eps = annual_financial_list[i+1].EPS
	print("EARNING -From "+ annual_financial_list[i].date + " to "+ annual_financial_list[i+1].date)
	print(((float(v2) - float(v1))/float(v1))* 100)
	print(((float(v2_eps) - float(v1_eps))/float(v1_eps))* 100)

