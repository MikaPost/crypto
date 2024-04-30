"""
This file is for our new theme: ?
Create by: Miqayel Postoyan
Date: 30 April
"""
import requests
import time


def print_cripto(data):
    """
    Function: print_cripto
    Brief: print data crypto
    Params: data
    Return:	None
    """
    for i in range(len(data)):
        print("Name: ", data[i]["name"])
        print("Symbol: ", data[i]["symbol"])
        print("Current Price: ", data[i]["priceUsd"], "$")
        print("Market Cap: ", data[i]["marketCapUsd"], "$")
        print("Total Volume: ", data[i]["volumeUsd24Hr"], "$")
        print("Price Change for 24 Hours: ", data[i]["changePercent24Hr"], "$", "\n")


def filter_name(datas, name):
    """
    Function: filter_name
    Brief: print name crypto
    Params: datas, name
    Return:	name crypto
    """
    return [i for i in datas if name.lower() in i["name"].lower()]

def filter_value(datas, value):
    """
    Function: filter_value
    Brief: print the cost of all cryptocurrencies is higher than value $
    Params: datas, value
    Return:	the cost of all cryptocurrencies is higher than value $
    """
    return [i for i in datas if float(i["priceUsd"]) > value]


def main():
    """
    Function: main
    Brief: Entry point
    """
    while True:
        url1 = "https://api.coincap.io/v2/assets"
        params = {"limit": 20}
        r = requests.get(url1, params=params)
        data = r.json()["data"]
        print_cripto(data)
        cripto = input("Enter crypto name and price: ")
        if cripto.isalpha():
            data = filter_name(data, cripto)
            print_cripto(data)
        elif cripto.isdigit():
            data = filter_value(data, float(cripto))
            print_cripto(data)
        time.sleep(5)


if __name__ == '__main__':
    main()
