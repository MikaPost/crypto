import requests
import time


def print_cripto(data):
    for i in range(len(data)):
        print("Name: ", data[i]["name"])
        print("Symbol: ", data[i]["symbol"])
        print("Current Price: ", data[i]["priceUsd"], "$")
        print("Market Cap: ", data[i]["marketCapUsd"], "$")
        print("Total Volume: ", data[i]["volumeUsd24Hr"], "$")
        print("Price Change for 24 Hours: ", data[i]["changePercent24Hr"], "$", "\n")


def filter_name(datas, name):
    return [i for i in datas if name.lower() in i["name"].lower()]

def filter_value(datas, value):
    return [i for i in datas if float(i["priceUsd"]) > value]


def main():
    url1 = "https://api.coincap.io/v2/assets"
    params = {"limit": 20}
    r = requests.get(url1, params=params)
    data = r.json()["data"]
    while True:
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
