import codecs
import csv

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

"""CoinMarketCap数据查询"""

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
parameters = {
    'start': '5000',
    'limit': '5000',
    'listing_status':'untracked',
}

proxies = {
    'http': 'http://127.0.0.1:7890/',
    'https': 'http://127.0.0.1:7890/'
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '07155bd2-e2ee-4eab-8777-2c846c1d2b16',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters, proxies=proxies)
    json_data = json.loads(response.text)
    data = json_data['data']

    data_file = open('D:\\7.23_coinmarketcap_api\\5000_10000_untracked.csv', 'w', encoding= 'utf-8', newline='')

    # create the csv writer object
    csv_writer = csv.writer(data_file)

    # Counter variable used for writing
    # headers to the CSV file
    count = 0

    for emp in data:
        if count == 0:
            # Writing headers of CSV file
            header = emp.keys()
            csv_writer.writerow(header)
            count += 1

        # Writing data of CSV file
        csv_writer.writerow(emp.values())

    data_file.close()
# tran_to_csv(path=path,jsonData= data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

