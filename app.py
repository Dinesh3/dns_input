import sqlite3
from db_con import create_dns_request
from flask import Flask, render_template, request

app = Flask(__name__)


# app.run(debug=True)
# app.run(use_reloader=True)


@app.route('/')
def index():
    return render_template("index1.html")

@app.route('/srv')
def srv():
    return render_template("srv.html")


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        print('hi', request)
        result = request.form
        print(result)
        # print(type(result))
        # print('ietns',result.items)
        # for key,value in result.items():
        #     print('data', value)
        form_data = tuple(None if x == '' else x for x in tuple(result.values()))

        print('d',form_data)
        connection  = sqlite3.connect('dns.db')
        row_id = create_dns_request(connection,form_data)
        print('row', row_id)
        return render_template("result.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)