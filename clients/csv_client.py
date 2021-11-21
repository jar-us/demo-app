import logging
import os
from collections.abc import MutableMapping

import coloredlogs
import pandas as pd

import nsedate as nd

coloredlogs.install(level='DEBUG')
logger = logging.getLogger(__name__)


def create_csv(json_file_name):
    # read json file
    df = pd.read_json(json_file_name)

    # get list of data from records
    rows = df['records']['data']

    # generate csv file name from json file name
    csv_file_name = generate_file_name(json_file_name)

    # all expiry dates before future date
    future_date = nd.futureDate()

    list_of_dicts = []

    for row in rows:
        expiryDate = row.get('expiryDate')
        # if expiryDate is before future_date
        if nd.convertToDateTime(expiryDate) <= future_date:
            # if file with name csv_file_name does not exist, then create
            if not os.path.isfile(csv_file_name):
                logger.warning("File does not exist, creating file=" + csv_file_name)
                flattened_row = flatten_dict(row)
                list_of_dicts.append(flattened_row)
                logger.info("Writing to file=" + csv_file_name)
                write_to_csv(list_of_dicts, csv_file_name, "w+")
            else:
                flattened_row = flatten_dict(row)
                list_of_dicts.append(flattened_row)
                logger.info("Updating the csv file=" + csv_file_name)
                write_to_csv(list_of_dicts, csv_file_name, "a")


def generate_file_name(json_file_name):
    date_month_year = json_file_name.split("-")
    return "csv/" + date_month_year[1] + "-" + date_month_year[2] + "-" + date_month_year[3] + "-" + \
           date_month_year[
               4] + ".csv"


def write_to_csv(list_of_dicts, file_name, mode):
    df = pd.DataFrame(list_of_dicts)
    df.to_csv(file_name, index=False, mode=mode)


def flatten_dict(d: MutableMapping, sep: str = '.') -> MutableMapping:
    [flat_dict] = pd.json_normalize(d, sep=sep).to_dict(orient='records')
    return flat_dict
