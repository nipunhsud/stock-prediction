import munch
import requests
import json

annual_response = requests.get("https://financialmodelingprep.com/api/v3/financials/income-statement/TSLA")

annual_data = annual_response.json()

annual_income_stmt = munch.Munch(annual_data)

# print(annual_income_stmt)
counter = 0
ranker = 1

for financial in annual_income_stmt.financials:
	if counter == 4 :
			break
	b = munch.Munch(financial)
	b.get('Revenue Growth')
	if float(b.get('Revenue Growth')) * 100 > 60 :
		ranker = ranker + 1

	counter = counter + 1
print(ranker)



# for i in range (len(annual_financial_list)-1):
# 	v2 = annual_financial_list[i].EBITDA
# 	v1 = annual_financial_list[i+1].EBITDA
# 	v2_eps = annual_financial_list[i].EPS
# 	v1_eps = annual_financial_list[i+1].EPS
# 	print("EARNING -From "+ annual_financial_list[i].date + " to "+ annual_financial_list[i+1].date)
# 	print(((float(v2) - float(v1))/float(v1))* 100)
# 	print(((float(v2_eps) - float(v1_eps))/float(v1_eps))* 100)

