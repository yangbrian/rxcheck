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
    cursor = client.rxcheck.medInfo.find({'brand_name': {
        '$regex': '^' + search
    }})

    def serialize(obj):
        return obj.__dict__

    return Response(response=dumps(cursor, default=serialize),
                    status=200,
                    mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
