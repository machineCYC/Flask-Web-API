import flask
import importlib

from flask import request

app = flask.Flask(__name__)

def show_Status(status_code):
    status_code_mapping = {
        200:"ok",
        400:"parameters error",
        404:"Server not found",
    }
    msg = {
        "status": status_code,
        "status_msg": status_code_mapping[status_code],
        "status_msg_desc":""
    }
    return msg

def get_Parameter(request):
    parameter = request.args
    dataset = parameter.get('Dataset', '')
    stock_id = parameter.get('StockId','')
    date = parameter.get('Date','2019-01-01')
    return dataset, stock_id, date

@app.route('/api/data', methods=['GET'])
def get_Data_Api():

    dataset, stock_id, date = get_Parameter(request)
    if dataset == '' or stock_id == '':
        msg = show_Status(status_code=400)
    else:
        Load = importlib.import_module("FinMind.Data.Load")
        data = Load.FinData(dataset=dataset, select=stock_id, date=date)

        if len(data) > 0:
            msg = show_Status(status_code=200)
            msg['data'] = {}
            for col in list(data.columns):
                msg['data'][col] = list(data[col])
        elif len(data) == 0:
            msg = show_Status(status_code=400)
    return msg

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"


if  __name__ == '__main__':
    app.run(debug=True)