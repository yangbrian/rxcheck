from flask import Flask, render_template, Response
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get/names/<search>')
def names(search):
    client = MongoClient("mongodb://localhost:27017")

    def getName(doc):
        return doc.brand_name

    cursor = client.rxcheck.medInfo.find({'brand_name': {
        '$regex': '^' + search
    }}, {'brand_name': 1}).distinct('brand_name')

    return Response(response=dumps(cursor),
                    status=200,
                    mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
