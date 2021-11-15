import pandas as pd
import datetime
import nsedate as nd
from pathlib import Path


def writeJsonToCsv(json_file_name):
    df = pd.read_json(json_file_name)
    # records = df.to_dict('records')
    data = df['records']['data']
    chain_date = []
    chain_time = []
    expiryDates = []
    strikePrices = []
    call_openInterests = []
    call_changeInOpenInterests = []
    call_percentageChangeInOpenInterests = []
    call_totalTradedVolume = []
    call_impliedVolatility = []
    call_lastPrice = []
    call_changeInLastPrice = []
    call_percentageChangeInLastPrice = []
    call_totalBuyQuantity = []
    call_totalSellQuantity = []
    call_bidQuantity = []
    call_bidPrice = []
    call_askQuantity = []
    call_askPrice = []
    call_underlyingValue = []

    put_openInterests = []
    put_changeInOpenInterests = []
    put_percentageChangeInOpenInterests = []
    put_totalTradedVolume = []
    put_impliedVolatility = []
    put_lastPrice = []
    put_changeInLastPrice = []
    put_percentageChangeInLastPrice = []
    put_totalBuyQuantity = []
    put_totalSellQuantity = []
    put_bidQuantity = []
    put_bidPrice = []
    put_askQuantity = []
    put_askPrice = []
    put_underlyingValue = []

    date_format = datetime.datetime.now().strftime("%Y-%m-%d")
    csv_file_name = "csv/" + "option-chain" + "-" + "nifty" + "-" + str(date_format) + ".csv"
    json_file_name_split = json_file_name.split("-")
    json_file_name_year = json_file_name_split[3]
    json_file_name_month = json_file_name_split[4]
    json_file_name_day = json_file_name_split[5]
    json_file_name_hours = json_file_name_split[6]
    json_file_name_minutes = json_file_name_split[7].split(".")[0]
    # csv_file_name = ""
    for d in data:
        expiryDate = d.get('expiryDate')
        if nd.convertToDateTime(expiryDate) < nd.futureDate():
            expiryDates.append(d.get('expiryDate'))
            strikePrices.append(d.get('strikePrice'))
            chain_date.append(json_file_name_day+"-"+json_file_name_month+"-"+json_file_name_year)
            chain_time.append(json_file_name_hours+":"+json_file_name_minutes)
            ce = d.get('CE', 'NA')
            pe = d.get('PE', 'NA')
            if ce != 'NA':
                call_openInterests.append(ce['openInterest'])
                call_changeInOpenInterests.append(ce['changeinOpenInterest'])
                call_percentageChangeInOpenInterests.append(ce['pchangeinOpenInterest'])
                call_totalTradedVolume.append(ce['totalTradedVolume'])
                call_impliedVolatility.append(ce['impliedVolatility'])
                call_lastPrice.append(ce['lastPrice'])
                call_changeInLastPrice.append(ce['change'])
                call_percentageChangeInLastPrice.append(ce['pChange'])
                call_totalBuyQuantity.append(ce['totalBuyQuantity'])
                call_totalSellQuantity.append(ce['totalSellQuantity'])
                call_bidQuantity.append(ce['bidQty'])
                call_bidPrice.append(ce['bidprice'])
                call_askQuantity.append(ce['askQty'])
                call_askPrice.append(ce['askPrice'])
                call_underlyingValue.append(ce['underlyingValue'])
            else:
                call_openInterests.append('NA')
                call_changeInOpenInterests.append('NA')
                call_percentageChangeInOpenInterests.append('NA')
                call_totalTradedVolume.append('NA')
                call_impliedVolatility.append('NA')
                call_lastPrice.append('NA')
                call_changeInLastPrice.append('NA')
                call_percentageChangeInLastPrice.append('NA')
                call_totalBuyQuantity.append('NA')
                call_totalSellQuantity.append('NA')
                call_bidQuantity.append('NA')
                call_bidPrice.append('NA')
                call_askQuantity.append('NA')
                call_askPrice.append('NA')
                call_underlyingValue.append('NA')
            if pe != 'NA':
                put_openInterests.append(pe['openInterest'])
                put_changeInOpenInterests.append(pe['changeinOpenInterest'])
                put_percentageChangeInOpenInterests.append(pe['pchangeinOpenInterest'])
                put_totalTradedVolume.append(pe['totalTradedVolume'])
                put_impliedVolatility.append(pe['impliedVolatility'])
                put_lastPrice.append(pe['lastPrice'])
                put_changeInLastPrice.append(pe['change'])
                put_percentageChangeInLastPrice.append(pe['pChange'])
                put_totalBuyQuantity.append(pe['totalBuyQuantity'])
                put_totalSellQuantity.append(pe['totalSellQuantity'])
                put_bidQuantity.append(pe['bidQty'])
                put_bidPrice.append(pe['bidprice'])
                put_askQuantity.append(pe['askQty'])
                put_askPrice.append(pe['askPrice'])
                put_underlyingValue.append(pe['underlyingValue'])
            else:
                put_openInterests.append('NA')
                put_changeInOpenInterests.append('NA')
                put_percentageChangeInOpenInterests.append('NA')
                put_totalTradedVolume.append('NA')
                put_impliedVolatility.append('NA')
                put_lastPrice.append('NA')
                put_changeInLastPrice.append('NA')
                put_percentageChangeInLastPrice.append('NA')
                put_totalBuyQuantity.append('NA')
                put_totalSellQuantity.append('NA')
                put_bidQuantity.append('NA')
                put_bidPrice.append('NA')
                put_askQuantity.append('NA')
                put_askPrice.append('NA')
                put_underlyingValue.append('NA')

    data1 = {
        'date': chain_date,
        'time': chain_time,
        'expiryDate': expiryDates,
        'strikePrice': strikePrices,

        'PE-openInterest': put_openInterests,
        'PE-changeInOpenInterest': put_changeInOpenInterests,
        'PE-pChangeInOpenInterest': put_percentageChangeInOpenInterests,
        'PE-totalTradedVolume': put_totalTradedVolume,
        'PE-impliedVolatility': put_impliedVolatility,
        'PE-lastPrice': put_lastPrice,
        'PE-changeInLastPrice': put_changeInLastPrice,
        'PE-pChangeInLastPrice': put_percentageChangeInLastPrice,
        'PE-totalBuyQuantity': put_totalBuyQuantity,
        'PE-totalSellQuantity': put_totalSellQuantity,
        'PE-bidQuantity': put_bidQuantity,
        'PE-bidPrice': put_bidPrice,
        'PE-askQuantity': put_askQuantity,
        'PE-askPrice': put_askPrice,
        'PE-underlyingValue': put_underlyingValue,

        'CE-openInterest': call_openInterests,
        'CE-changeInOpenInterest': call_changeInOpenInterests,
        'CE-pChangeInOpenInterest': call_percentageChangeInOpenInterests,
        'CE-totalTradedVolume': call_totalTradedVolume,
        'CE-impliedVolatility': call_impliedVolatility,
        'CE-lastPrice': call_lastPrice,
        'CE-changeInLastPrice': call_changeInLastPrice,
        'CE-pChangeInLastPrice': call_percentageChangeInLastPrice,
        'CE-totalBuyQuantity': call_totalBuyQuantity,
        'CE-totalSellQuantity': call_totalSellQuantity,
        'CE-bidQuantity': call_bidQuantity,
        'CE-bidPrice': call_bidPrice,
        'CE-askQuantity': call_askQuantity,
        'CE-askPrice': call_askPrice,
        'CE-underlyingValue': call_underlyingValue,
    }
    # check if file exists
    Path(csv_file_name).touch(exist_ok=True)

    pd.DataFrame(data1).to_csv(csv_file_name, index=False, mode='a')

    print(csv_file_name + " updated Successfully")
