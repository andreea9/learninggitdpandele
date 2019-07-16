import requests
import csv

class GetStockFinance(object):

    def __init__(self, url, stockindex):
        self.url = url
        self.stockindex = stockindex

    def get_stock_finance(self):
        download = requests.get(self.url+self.stockindex+'.csv')
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        return list(cr)

class WriteToCsv(object):

    def __init__(self, filename):
        self.filename = filename

    def write_to_csv(self, continut):
        with open(self.filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(continut)


a = GetStockFinance('https://www.quandl.com/api/v3/datasets/WIKI/','AAPL')
csv_de_scris = a.get_stock_finance()
b = WriteToCsv('test.csv')
b.write_to_csv(csv_de_scris)