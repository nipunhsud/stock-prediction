
import time
import qagr
import annualized_growth_rate as annual
import cagr
import cup
import market_cap_pe
import key_metric
from result import Result


def sort_and_print(result_list):
  
  for result in result_list:
    
    if result.annualized_growth_rate is not None:
      print("AGR: ", str("{:,.2f}".format(result.annualized_growth_rate)))
    if result.qagr is not None:
      print("QAGR: ", str("{:,.2f}".format(result.qagr)))
    if result.cagr is not None:
      print("CAGR: ", str("{:,.2f}".format(result.cagr)))
    print("CUP: ", result.cup)
    if result.key_metric.market_cap is not None:
      print("Market Cap: ", str("{:,.2f}".format(result.key_metric.market_cap)))
    if result.key_metric.pe is not None:
      print("PE: ", str("{:,.2f}".format(result.key_metric.pe)))
      
  
def analyze_stocks(symbolsList):
  
  for symbol in symbolsList:
    sym = ""
    if isinstance(symbol, str):
        sym = symbol
    # print(symbols.get('symbol'))
    
    # if(symbols.get('exchange') == 'Toronto'):
      # sym = symbols.get('symbol').split(".")
    else:
      if(symbol.get('exchange') == 'New York Stock Exchange' or symbol.get('exchange') == 'Nasdaq Global Select'):
        sym = symbol.get('symbol')
      
    print(sym)
    time.sleep(2)
    
    result_list= []
    result_list.append(Result(qagr.calc_eps(sym),annual.calc_annual_eps(sym), cagr.calc_cagr(
        sym), cup.analyze(sym), market_cap_pe.perform(sym)))
    # if quaterly_eps is not None:
      
      
    sort_and_print(result_list)
    
