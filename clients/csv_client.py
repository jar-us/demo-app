import pandas as pd
import os
import nsedate as nd


#
# def update_csv():
#     print("Updating CSV file...")


# take json file name as input and file name format is json/oc-dd-mm-yyyy-hh-mm.json
# get date and month and year from json file name
# create csv file name with date and month and year,  eg cv/oc-dd-mm-yyyy.csv
# read json file
# if csv file with same date and month and year does not exist, create csv file and return -> created
# if csv file with same date and month and year exists, append json data to csv file -> updated
def create_csv(json_file_name):
    date_month_year = json_file_name.split("-")
    print(date_month_year)
    csv_file_name = "csv/" + date_month_year[1] + "-" + date_month_year[2] + "-" + date_month_year[3] + "-" + \
                    date_month_year[
                        4] + ".csv"
    print("Creating CSV file: " + csv_file_name)
    # load json file using pandas
    df = pd.read_json(json_file_name)
    # convert df to dict
    records = df['records']['data']


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
    # if csv file with same date and month and year does not exist, create csv file and return -> created
    if not os.path.exists(csv_file_name):
        # create csv file
        for record in records:
            if nd.convertToDateTime(record.get('expiryDate')) < nd.futureDate():
                expiryDates.append(record.get('expiryDate'))
                strikePrices.append(record.get('strikePrice'))
                ce = record.get('CE', 'NA')
                pe = record.get('PE', 'NA')
                if ce != 'NA':
                                  call_openInterests.append(ce.get('openInterest'))
                                  call_changeInOpenInterests.append(ce.get('changeInOpenInterest'))
                                  call_percentageChangeInOpenInterests.append(ce.get('percentageChangeInOpenInterest'))
                                  call_totalTradedVolume.append(ce.get('totalTradedVolume'))
                                  call_impliedVolatility.append(ce.get('impliedVolatility'))
                                  call_lastPrice.append(ce.get('lastPrice'))
                                  call_changeInLastPrice.append(ce.get('changeInLastPrice'))
                                  call_percentageChangeInLastPrice.append(ce.get('percentageChangeInLastPrice'))
                                  call_totalBuyQuantity.append(ce.get('totalBuyQuantity'))
                                  call_totalSellQuantity.append(ce.get('totalSellQuantity'))
                                  call_bidQuantity.append(ce.get('bidQuantity'))
                                  call_bidPrice.append(ce.get('bidPrice'))
                                  call_askQuantity.append(ce.get('askQuantity'))
                                  call_askPrice.append(ce.get('askPrice'))
                                  call_underlyingValue.append(ce.get('underlyingValue'))
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
                                  put_openInterests.append(pe.get('openInterest'))
                                  put_changeInOpenInterests.append(pe.get('changeInOpenInterest'))
                                  put_percentageChangeInOpenInterests.append(pe.get('percentageChangeInOpenInterest'))
                                  put_totalTradedVolume.append(pe.get('totalTradedVolume'))
                                  put_impliedVolatility.append(pe.get('impliedVolatility'))
                                  put_lastPrice.append(pe.get('lastPrice'))
                                  put_changeInLastPrice.append(pe.get('changeInLastPrice'))
                                  put_percentageChangeInLastPrice.append(pe.get('percentageChangeInLastPrice'))
                                  put_totalBuyQuantity.append(pe.get('totalBuyQuantity'))
                                  put_totalSellQuantity.append(pe.get('totalSellQuantity'))
                                  put_bidQuantity.append(pe.get('bidQuantity'))
                                  put_bidPrice.append(pe.get('bidPrice'))
                                  put_askQuantity.append(pe.get('askQuantity'))
                                  put_askPrice.append(pe.get('askPrice'))
                                  put_underlyingValue.append(pe.get('underlyingValue'))
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
        series = {
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
        pd.DataFrame(series).to_csv(csv_file_name, index=False, mode='w')
        return "created"
    # if csv file with same date and month and year exists, append json data to csv file -> updated
    else:
        for record in records:
            if nd.convertToDateTime(record.get('expiryDate')) < nd.futureDate():
                expiryDates.append(record.get('expiryDate'))
                strikePrices.append(record.get('strikePrice'))
                ce = record.get('CE', 'NA')
                pe = record.get('PE', 'NA')
                if ce != 'NA':
                    call_openInterests.append(ce.get('openInterest'))
                    call_changeInOpenInterests.append(ce.get('changeInOpenInterest'))
                    call_percentageChangeInOpenInterests.append(ce.get('percentageChangeInOpenInterest'))
                    call_totalTradedVolume.append(ce.get('totalTradedVolume'))
                    call_impliedVolatility.append(ce.get('impliedVolatility'))
                    call_lastPrice.append(ce.get('lastPrice'))
                    call_changeInLastPrice.append(ce.get('changeInLastPrice'))
                    call_percentageChangeInLastPrice.append(ce.get('percentageChangeInLastPrice'))
                    call_totalBuyQuantity.append(ce.get('totalBuyQuantity'))
                    call_totalSellQuantity.append(ce.get('totalSellQuantity'))
                    call_bidQuantity.append(ce.get('bidQuantity'))
                    call_bidPrice.append(ce.get('bidPrice'))
                    call_askQuantity.append(ce.get('askQuantity'))
                    call_askPrice.append(ce.get('askPrice'))
                    call_underlyingValue.append(ce.get('underlyingValue'))
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
                    put_openInterests.append(pe.get('openInterest'))
                    put_changeInOpenInterests.append(pe.get('changeInOpenInterest'))
                    put_percentageChangeInOpenInterests.append(pe.get('percentageChangeInOpenInterest'))
                    put_totalTradedVolume.append(pe.get('totalTradedVolume'))
                    put_impliedVolatility.append(pe.get('impliedVolatility'))
                    put_lastPrice.append(pe.get('lastPrice'))
                    put_changeInLastPrice.append(pe.get('changeInLastPrice'))
                    put_percentageChangeInLastPrice.append(pe.get('percentageChangeInLastPrice'))
                    put_totalBuyQuantity.append(pe.get('totalBuyQuantity'))
                    put_totalSellQuantity.append(pe.get('totalSellQuantity'))
                    put_bidQuantity.append(pe.get('bidQuantity'))
                    put_bidPrice.append(pe.get('bidPrice'))
                    put_askQuantity.append(pe.get('askQuantity'))
                    put_askPrice.append(pe.get('askPrice'))
                    put_underlyingValue.append(pe.get('underlyingValue'))
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
        series = {
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
        pd.DataFrame(series).to_csv(csv_file_name, index=False, mode='w')
        return "updated"


# # create a method should accept json object and update csv file
# def write_to_csv(file_name):
#     # load json file using pandas
#     df = pd.read_json(file_name)
#     # convert df to dict
#     df_dict = df.to_dict()
