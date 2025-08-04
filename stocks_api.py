import requests


def stocks_info():
    url = "https://api.freeapi.app/api/v1/public/stocks/stock/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        stock_data = data["data"]
        company_name = stock_data["Name"]
        stock_listing_date = stock_data["ListingDate"]
        stock_id = stock_data["ISIN"]
        stock_roe = stock_data["ROE"]
        stock_roce = stock_data["ROCE"]
        stock_mkt_cap = stock_data["MarketCap"]
        stock_cp = stock_data["CurrentPrice"]

        return company_name, stock_listing_date, stock_id, stock_roe, stock_roce, stock_mkt_cap, stock_cp
    else:
        # raise ConnectionError("failed to fetch the stock")
        raise Exception("failed please check your internet connection")


def main():
    try:
        company_name, stock_listing_date, stock_id, stock_roe, stock_roce, stock_mkt_cap, stock_cp = stocks_info()
        print(f"\nName: {company_name} \nCurrentPrice: {stock_cp} \nListingDate: {stock_listing_date} \nISIN: {stock_id} \nReturn of investment: {stock_roe} \nMarket Cap: {stock_mkt_cap} \nROCE: {stock_roce}")
    except Exception as pablo:
            print(str(pablo))


if __name__ == main():
    main()