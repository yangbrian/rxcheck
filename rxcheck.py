from flask import Flask, render_template, Response, request
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
        '$regex': '.*' + search
    }}, {'brand_name': 1}).distinct('brand_name')

    return Response(response=dumps(cursor),
                    status=200,
                    mimetype="application/json")

@app.route('/post/email/', methods=['POST'])
def uploadEmail():
    userInfo = {'phone': request.form['phone'],
                'email': request.form['email']}
    drugs = request.form['drugs'].split(',')

    #Connect to mongodb client
    client = MongoClient('localhost', 27017)

    #Get the database
    db = client.rxcheck

    #Get the collection
    collection = db.emailInfo

    for drug in drugs:
        collection.find_one_and_update(
            {'drug_name': drug},
            {'$push': {'users': userInfo}})

    return Response(response='',
                    status=200,
                    mimetype="application/json")


@app.route('/get/warnings/<name>')
def warnings(name):
    client = MongoClient("mongodb://localhost:27017")

    cursor = client.rxcheck.medInfo.find_one({'brand_name': {
        '$regex': '^' + name
            }}, {'brand_name': 1,
                 'generic_name': 1,
                 'warnings_and_precautions': 1,
                 'warnings': 1,
                 'active_ingredient': 1,
                 'inactive_ingredient': 1})

    return Response(response=dumps(cursor),
                    status=200,
                    mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
