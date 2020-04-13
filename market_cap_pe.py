import munch
import requests
import json
from key_metric import KeyMetric


def perform(stock):
  response = requests.get('https://fmpcloud.io/api/v3/key-metrics/{}?apikey=e5ccbcc74abe54698f96836dd4c51d48'.format(stock))

  key_metrics = response.json()

  # print('PE '+ str(key_metrics[0].get('peRatio')))
  # print('Market Cap ' + str("{:,}".format(key_metrics[0].get('marketCap'))))

  return KeyMetric(key_metrics[0].get('marketCap'), key_metrics[0].get('peRatio'))