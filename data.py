from __future__ import print_function
import time
import intrinio_sdk
from intrinio_sdk.rest import ApiException
from pprint import pprint

intrinio_sdk.ApiClient(
).configuration.api_key['api_key'] = 'OjU1ZGI0NTNhMzZiOWViNmRjMWM4YjEyYWMwMDdkMjNj'

security_api = intrinio_sdk.SecurityApi()

# str | A Security identifier (Ticker, FIGI, ISIN, CUSIP, Intrinio ID)
identifier = 'AAPL'
# int | The number of results to return (optional) (default to 100)
page_size = 500
# str | Gets the next page of data from a previous API call (optional)
next_page = ''

try:
  api_response = security_api.get_security_zacks_eps_surprises(
      identifier, page_size=page_size, next_page=next_page)
  pprint(api_response)
except ApiException as e:
  print("Exception when calling SecurityApi->get_security_zacks_eps_surprises: %s\r\n" % e)
