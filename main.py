import requests

def main():
    url1 = "https://api.coincap.io/v2/assets"
    params = {"limit": 100}
    r = requests.get(url1, params=params)
    print(r.json())
    print(r.request.url)


if __name__ == '__main__':
    main()
