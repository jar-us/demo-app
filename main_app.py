# print hello world in main method
from clients import web_client as wc
from clients import csv_client as cc

# def main():
#     print("Hello World")


if __name__ == "__main__":
    # json_file_status = wc.option_chain_data()
    # print(json_file_status)
    cc.create_csv("json/oc-NIFTY-16-11-2021-15-30.json")

    # main()
