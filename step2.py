import munch
import requests
import json

def get_rank(data, key) :
	# print(data)
	counter = 0
	revenue_growth_ranker = 0
	for financial in data :
	
		if counter == 4 :
			break

		b = munch.Munch(financial)
		print(b.get(key))
		if float(b.get(key)) * 100 > 60 :
			revenue_growth_ranker = revenue_growth_ranker + 1


		counter = counter + 1
	print("revenue_growth_ranker "+ str(revenue_growth_ranker))




annual_response = requests.get("https://financialmodelingprep.com/api/v3/financials/income-statement/TSLA")
annual_data = annual_response.json()
annual_income_stmt = munch.Munch(annual_data)
# print(annual_income_stmt)
# get_rank(annual_income_stmt.financials, 'Revenue Growth')



annual_response = requests.get("https://financialmodelingprep.com/api/v3/financial-statement-growth/SHOP")
annual_data = annual_response.json()
annual_income_stmt = munch.Munch(annual_data)

# print(annual_income_stmt)
# print (annual_income_stmt.growth)
# get_rank(annual_income_stmt.growth, 'Gross Profit Growth')
# get_rank(annual_income_stmt.growth, 'EBIT Growth')
get_rank(annual_income_stmt.growth, 'EPS Growth')




# for i in range (len(annual_financial_list)-1):
# 	v2 = annual_financial_list[i].EBITDA
# 	v1 = annual_financial_list[i+1].EBITDA
# 	v2_eps = annual_financial_list[i].EPS
# 	v1_eps = annual_financial_list[i+1].EPS
# 	print("EARNING -From "+ annual_financial_list[i].date + " to "+ annual_financial_list[i+1].date)
# 	print(((float(v2) - float(v1))/float(v1))* 100)
# 	print(((float(v2_eps) - float(v1_eps))/float(v1_eps))* 100)

# 