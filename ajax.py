# 處理回傳資料
from flask import Flask, render_template, request, jsonify, json

app = Flask(__name__)


@app.route('/data')
def webapi():
    return render_template('data.html')


@app.route('/data/message', methods=['GET'])
def getDataMessage():
    if request.method == "GET":
        with open('static/data/message.json', 'r') as f:
            data = json.load(f)
            print("text : ", data)
        f.close
        return jsonify(data)  # 直接回傳 data 也可以，都是 json 格式


@app.route('/data/message', methods=['POST'])
def setDataMessage():
    if request.method == "POST":
        data = {
            'appInfo': {
                'id': request.form['app_id'],
                'name': request.form['app_name'],
                'version': request.form['app_version'],
                'author': request.form['app_author'],
                'remark': request.form['app_remark']
            }
        }
        print(type(data))
        with open('static/data/input.json', 'w') as f:
            json.dump(data, f) # 使用 json 物件，寫入 json 文字格式到 input.json 檔案
        f.close
        return jsonify(result='OK')


if __name__ == '__main__':
    app.run()