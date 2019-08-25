import requests


url = 'http://127.0.0.1:5000/api/data'
# url = 'http://127.0.0.1:5000/api/data?Dataset=TaiwanStockPrice&StockId=2330&Date=2018-01-01'

dataset = 'TaiwanStockPrice'
stock_id = '2330'
date = '2018-01-01'
parameter = {
    'Dataset':dataset,
    'StockId':stock_id,
    'Date': date,
}

res = requests.get(url, params=parameter)
data = res.json()

print('GG')