import requests
import json

class Financial(object):
    def __init__(self, financial):
        self.financial = financial
        self.date = financial['date']
        self.eps = financial['EPS']

response = requests.get("https://financialmodelingprep.com/api/v3/financials/income-statement/AAPL?period=quarter")
print(response.headers['Content-Type'])
text = json.dumps(response.json(), sort_keys=True, indent=4)
# print(text)

def as_payload(dct):
    return Financial(dct)

# financials = json.loads(response.json(), object_hook = as_payload)

print('financials' in text)

data = response.json()
# print(financials)

financials = data['financials']
print(financials)
for financial in financials:
    financial = as_payload(financial)
    print(financial.eps)

# print(text)
# financials_list = Financials(response.json())
# print (data)
# print(data)

# print(text['Valuation Ratio']['PS Ratio'])

# financials = financials_list.financials()

for financial in financials:
    print(financial['date'])

# print text.get("annuals", "none")
# print('annuals' in data)

key_ratio_response = requests.get("https://api.gurufocus.com/public/user/e0d5da606d04986259029c378f0dd988:ff2c47bd5dd6118c41dadaf99fec76f7/stock/EAF/keyratios")

text = json.dumps(key_ratio_response.json(), sort_keys=True, indent=4)
# print(text)
