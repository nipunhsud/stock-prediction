import munch
import requests
import json

# Gets the average annual eps growth over 5 years
def get_annualized_growth_rate(data, key) :
	# print(data)
	counter = 0
	growth = 0
	for financial in data :
	
		if counter == 5 :
			break

		b = munch.Munch(financial)
		eps_growth = b.get(key)					
		
		if eps_growth != '' and eps_growth != '0.0':
			# print(float(b.get(key)))
			growth = growth + float(b.get(key))
			# print(growth)
			counter = counter + 1
	annualized_growth_rate = growth/5 * 100
	print("Annualized Growth Rate %"+ str(annualized_growth_rate))


def calc_annual_eps(stock):
	annual_response = requests.get("https://financialmodelingprep.com/api/v3/financial-statement-growth/{}".format(stock))
	annual_data = annual_response.json()
	annual_income_stmt = munch.Munch(annual_data)

	# Creates a ranker - this measures if EPS growth is more than 60%
	if 'growth' in annual_income_stmt:
		get_annualized_growth_rate(annual_income_stmt.growth, 'EPS Growth')
