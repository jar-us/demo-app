import logging
import time
import coloredlogs
import schedule
from clients import csv_client as cc
from clients import web_client as wc

coloredlogs.install(level='DEBUG')
logger = logging.getLogger(__name__)


def option_chain_data():
    json_file_status = wc.option_chain_data()
    logger.info('From webclient: {}'.format(json_file_status))
    logger.info("===========================================================================")

    if json_file_status.startswith("CREATED"):
        created_csv = cc.create_csv(json_file_status.split('_')[1])
    else:
        logger.warning("No Data from NSE")


if __name__ == "__main__":
    while True:
        try:
            option_chain_data()
        except Exception as e:
            logger.error("Error in main_app.py = " + str(e))
        finally:
            time.sleep(120)
