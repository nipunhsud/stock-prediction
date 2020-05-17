
import time
import qagr
import annualized_growth_rate as annual
import cagr
import cup
import market_cap_pe
import key_metric
from result import Result


def sort_and_print(result_list):

    result_list.sort(key=lambda x: x.cagr, reverse=True)

    for result in result_list:

        print("TICKER: ", result.sym)
        print("NAME: ", result.name)
        if result.annualized_growth_rate is not None:
            print("AGR: ", str("{:,.2f}".format(
                result.annualized_growth_rate)))
        if result.qagr is not None:
            print("QAGR: ", str("{:,.2f}".format(result.qagr)))
        if result.cagr is not None:
            print("CAGR: ", str("{:,.2f}".format(result.cagr)))
        print("CUP: ", result.cup)
        if result.key_metric.market_cap is not None:
            print("Market Cap (MM): ", str("{:,.2f}".format(
                result.key_metric.market_cap/1000000)))
        if result.key_metric.pe is not None:
            print("PE: ", str("{:,.2f}".format(result.key_metric.pe)))


def analyze_stocks(symbolsList):
    print(symbolsList)
    result_list = []
    for symbol in symbolsList:
        time.sleep(2)
        sym = ""
        name = ""
        if isinstance(symbol, str):
            sym = symbol
            name = sym

        else:
            # if(symbol.get('exchange') != 'NYSE Arca' or symbol.get('exchange') == 'Nasdaq Global Select'):
            sym = symbol.get('symbol')
            name = symbol.get('name')
                # print(symbol.get('exchange'))

        if sym != "":

            result = Result(sym, name, qagr.calc_eps(sym), annual.calc_annual_eps(sym), cagr.calc_cagr(
                sym), cup.analyze(sym), market_cap_pe.perform(sym))
            if (result.cagr is not None and result.key_metric.pe is not None and not isinstance(result.cagr, complex) and result.cagr > 20 and result.key_metric.pe < 30 and result.annualized_growth_rate is not None and result.annualized_growth_rate > 0 and result.qagr is not None and result.qagr > 0):
                result_list.append(result)
            # if quaterly_eps is not None:
                # print(len(result_list))

    sort_and_print(result_list)
